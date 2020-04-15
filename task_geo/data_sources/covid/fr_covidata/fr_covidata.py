"""
fr_covidata.py

Functions:
    - fr_covidata_connector: Extracts data from CSV URL
    - fr_covidata_formatter: Cleans CSV data
    - fr_covidata: Combines the two previous functions

Data Credits:
    OpenCOVID19-fr
    https://www.data.gouv.fr/en/datasets/chiffres-cles-concernant-lepidemie-de-covid19-en-france/
    https://github.com/opencovid19-fr/data
"""

import io

import numpy as np
import pandas as pd
import requests

url = (
    'https://raw.githubusercontent.com/opencovid19-fr/'
    'data/master/dist/chiffres-cles.csv'
)


def fr_covidata():
    """Data Source for the French COVID-19 Data.
    Arguments:
        None
    Returns:
        pandas.DataFrame
    """
    df = fr_covidata_connector()
    return fr_covidata_formatter(df)


def fr_covidata_connector():
    """Extract data from OpenCOVID19-fr's Github repository.
    Description:
        - Downloads the URL's data in a Unicode CSV Format
        - Unicode CSV Format: ACS 5Y UTF-8
    Returns:
        dataset (DataFrame with CSV Data)
    """

    urlData = requests.get(url).content

    dataset = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    return dataset


def fr_covidata_formatter(dataset):
    """Formatter for FR COVID-19 Data.
    Arguments:
        dataset(pandas.DataFrame): Data as returned by fr_covidata_connector.
    Description:
        - Drop unnecessary rows with irrelevant regions' info and only keep
        info related to subregions in Metropolitan France, as well as
        repetitive data
        - Check the dataset for instances where there are more than one source
        of data in the same subregion for the same date, then complement all
        the sources information, and take the highest value in case there are
        different values for the same column, while aggregating the sources
        info
        - Rename/Translate the column titles, and add a country column (France)
    Returns:
        frcovidata(pandas.DataFrame)
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
    str_columns = ['source_nom', 'source_url',
                   'source_archive', 'source_type']
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
    dataset = dataset.groupby(['date',
                               'maille_code',
                               'maille_nom']).aggregate(aggre).reset_index()

    # Rename/Translate the column titles:
    dataset = dataset.rename(
        columns={"maille_code": "subregion_code",
                 "maille_nom": "subregion_name", "cas_confirmes": "confirmed",
                 "deces": "deaths", "reanimation": "recovering",
                 "hospitalises": "hospitalized", "gueris": "recovered",
                 "source_nom": "source_name"})
    dataset['country'] = 'France'
    frcovidata = dataset[
        'subregion_code', 'subregion_name', 'country', 'date', 'confirmed',
        'hospitalized', 'recovering', 'recovered',
        'deaths', 'source_name', 'source_url', 'source_archive',
        'source_type']

    return frcovidata
