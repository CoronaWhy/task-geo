import numpy as np
import pandas as pd


def fr_covid_formatter(dataset):
    """Formatter for FR COVID-19 Data.

    Description:

        - Drop unnecessary rows with irrelevant regions' info and only keep
          info related to subregions in Metropolitan France, as well as
          repetitive data.
        - Check the dataset for instances where there are more than one source
          of data in the same subregion for the same date, then complement all
          the sources information, and take the highest value in case there are
          different values for the same column, while aggregating the sources info
        - Rename/Translate the column titles, and add a country column (France)


    Arguments:
        dataset(pandas.DataFrame): Data as returned by fr_covidata_connector.

    Returns:
        pandas.DataFrame

    """
    no_gr = ['region', 'monde', 'pays', 'collectivite-outremer']
    no_mc = ['DEP-971', 'DEP-972', 'DEP-973', 'DEP-974', 'DEP-976']
    dataset = dataset[
        (~dataset.granularite.isin(no_gr)) & (~dataset.maille_code.isin(no_mc))
    ]
    dataset = dataset.drop(['depistes', 'granularite'], axis=1)
    dataset = dataset.drop_duplicates(
        subset=['date', 'maille_code', 'cas_confirmes', 'deces',
                'reanimation',
                'hospitalises', 'gueris'], keep=False)
    dataset['date'] = pd.to_datetime(dataset['date'].astype(str)).dt.date

    # Reset indices:
    dataset = dataset.reset_index(drop=True)

    # Turn source columns' values type to string:
    str_columns = ['source_nom', 'source_url', 'source_archive', 'source_type']
    dataset[str_columns] = dataset[str_columns].astype(str)

    aggre = {
        'cas_confirmes': np.max,
        'cas_ehpad': np.max,
        'cas_confirmes_ehpad': np.max,
        'cas_possibles_ehpad': np.max,
        'deces': np.max,
        'deces_ehpad': np.max,
        'reanimation': np.max,
        'hospitalises': np.max,
        'gueris': np.max,
        'source_nom': ','.join,
        'source_url': ','.join,
        'source_archive': ','.join,
        'source_type': ','.join
    }

    group_columns = ['date', 'maille_code', 'maille_nom']
    dataset = dataset.groupby(group_columns).aggregate(aggre).reset_index()

    # Rename/Translate the column titles:
    renamed_columns = {
        "maille_code": "subregion_code",
        "maille_nom": "subregion_name", "cas_confirmes": "confirmed",
        "deces": "deaths", "reanimation": "recovering",
        "hospitalises": "hospitalized", "gueris": "recovered",
        "source_nom": "source_name"
    }
    dataset = dataset.rename(columns=renamed_columns)
    dataset['country'] = 'France'
    frcovidata = dataset[
        'subregion_code', 'subregion_name', 'country', 'date', 'confirmed',
        'hospitalized', 'recovering', 'recovered',
        'deaths', 'source_name', 'source_url', 'source_archive',
        'source_type']

    return frcovidata
