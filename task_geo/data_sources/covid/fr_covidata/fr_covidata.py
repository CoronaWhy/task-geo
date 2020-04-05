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

    dataset = dataset[dataset.granularite != 'region']
    dataset = dataset[dataset.granularite != 'monde']
    dataset = dataset[dataset.granularite != 'pays']
    dataset = dataset[dataset.granularite != 'collectivite-outremer']
    dataset = dataset[dataset.maille_code != 'DEP-971']
    dataset = dataset[dataset.maille_code != 'DEP-972']
    dataset = dataset[dataset.maille_code != 'DEP-973']
    dataset = dataset[dataset.maille_code != 'DEP-974']
    dataset = dataset[dataset.maille_code != 'DEP-976']
    dataset = dataset.drop(['depistes'], axis=1)
    dataset = dataset.drop(['granularite'], axis=1)
    dataset = dataset.drop_duplicates(
        subset=['date', 'maille_code', 'cas_confirmes', 'deces',
                'reanimation',
                'hospitalises', 'gueris'], keep=False)

    # Reset indices:
    dataset = dataset.reset_index()
    dataset = dataset.drop(['index'], axis=1)

    # Turn source columns' values type to string:
    dataset['source_nom'] = dataset['source_nom'].astype(str)
    dataset['source_url'] = dataset['source_url'].astype(str)
    dataset['source_archive'] = dataset['source_archive'].astype(str)
    dataset['source_type'] = dataset['source_type'].astype(str)

    for i in range(len(dataset) - 1):
        if dataset.loc[i, 'maille_code'] == dataset.loc[
            i + 1, 'maille_code'] and dataset.loc[i, 'date'] == dataset.loc[
            i + 1, 'date'] and dataset.loc[
                i, 'cas_confirmes'] != 'inv' and i != len(dataset):
            # Combine Source names, url, archive and type for repetitive
            # subregions at the same date:
            dataset.loc[i, 'source_nom'] = dataset.loc[i, 'source_nom'] + \
                                           dataset.loc[i + 1, 'source_nom']
            dataset.loc[i, 'source_url'] = dataset.loc[i, 'source_url'] + \
                dataset.loc[i + 1, 'source_url']
            dataset.loc[i, 'source_archive'] = dataset.loc[
                                                   i, 'source_archive'] + \
                dataset.loc[
                                                   i + 1, 'source_archive']
            dataset.loc[i, 'source_type'] = dataset.loc[i, 'source_type'] + \
                dataset.loc[i + 1, 'source_type']
            if pd.isnull(
                    dataset.loc[i, 'cas_confirmes']) is True and pd.isnull(
                    dataset.loc[i + 1, 'cas_confirmes']) is False:
                    dataset.loc[i, 'cas_confirmes'] = dataset.loc[
                                                        i + 1, 'cas_confirmes']
                    dataset.loc[i + 1, 'cas_confirmes'] = 'inv'
            elif pd.isnull(
                    dataset.loc[i, 'cas_confirmes']) is False and pd.isnull(
                    dataset.loc[i + 1, 'cas_confirmes']) is True:
                        dataset.loc[i + 1, 'cas_confirmes'] = 'inv'
            elif pd.isnull(
                    dataset.loc[i, 'cas_confirmes']) is True and pd.isnull(
                    dataset.loc[i + 1, 'cas_confirmes']) is True:
                        dataset.loc[i + 1, 'cas_confirmes'] = 'inv'
            elif dataset.loc[i, 'cas_confirmes'] == dataset.loc[
                                                    i + 1, 'cas_confirmes']:
                dataset.loc[i + 1, 'cas_confirmes'] = 'inv'
            elif dataset.loc[i, 'cas_confirmes'] > dataset.loc[
                                                    i + 1, 'cas_confirmes']:
                dataset.loc[i + 1, 'cas_confirmes'] = 'inv'
            elif dataset.loc[i, 'cas_confirmes'] < dataset.loc[
                                                    i + 1, 'cas_confirmes']:
                dataset.loc[i, 'cas_confirmes'] = dataset.loc[
                    i + 1, 'cas_confirmes']
                dataset.loc[i + 1, 'cas_confirmes'] = 'inv'

        if dataset.loc[i, 'maille_code'] == dataset.loc[
            i + 1, 'maille_code'] and dataset.loc[i, 'date'] == dataset.loc[
                i + 1, 'date'] and dataset.loc[i, 'deces'] != 'inv':
            if pd.isnull(dataset.loc[i, 'deces']) is True and pd.isnull(
                    dataset.loc[i + 1, 'deces']) is False:
                dataset.loc[i, 'deces'] = dataset.loc[i + 1, 'deces']
                dataset.loc[i + 1, 'deces'] = 'inv'
            elif pd.isnull(dataset.loc[i, 'deces']) is False and pd.isnull(
                    dataset.loc[i + 1, 'deces']) is True:
                dataset.loc[i + 1, 'deces'] = 'inv'
            elif pd.isnull(dataset.loc[i, 'deces']) is True and pd.isnull(
                    dataset.loc[i + 1, 'deces']) is True:
                dataset.loc[i + 1, 'deces'] = 'inv'
            elif dataset.loc[i, 'deces'] == dataset.loc[i + 1, 'deces']:
                dataset.loc[i + 1, 'deces'] = 'inv'
            elif dataset.loc[i, 'deces'] > dataset.loc[i + 1, 'deces']:
                dataset.loc[i + 1, 'deces'] = 'inv'
            elif dataset.loc[i, 'deces'] < dataset.loc[i + 1, 'deces']:
                dataset.loc[i, 'deces'] = dataset.loc[i + 1, 'deces']
                dataset.loc[i + 1, 'deces'] = 'inv'

        if dataset.loc[i, 'maille_code'] == dataset.loc[
            i + 1, 'maille_code'] and dataset.loc[i, 'date'] == dataset.loc[
                i + 1, 'date'] and dataset.loc[i, 'reanimation'] != 'inv':
            if pd.isnull(dataset.loc[i, 'reanimation']) is True and pd.isnull(
                    dataset.loc[i + 1, 'reanimation']) is False:
                dataset.loc[i, 'reanimation'] = dataset.loc[
                    i + 1, 'reanimation']
                dataset.loc[i + 1, 'reanimation'] = 'inv'
            elif pd.isnull(
                    dataset.loc[i, 'reanimation']) is False and pd.isnull(
                        dataset.loc[i + 1, 'reanimation']) is True:
                dataset.loc[i + 1, 'reanimation'] = 'inv'
            elif pd.isnull(
                    dataset.loc[i, 'reanimation']) is True and pd.isnull(
                        dataset.loc[i + 1, 'reanimation']) is True:
                dataset.loc[i + 1, 'reanimation'] = 'inv'
            elif dataset.loc[i, 'reanimation'] == dataset.loc[
                                                    i + 1, 'reanimation']:
                dataset.loc[i + 1, 'reanimation'] = 'inv'
            elif dataset.loc[i, 'reanimation'] > dataset.loc[
                                                    i + 1, 'reanimation']:
                dataset.loc[i + 1, 'reanimation'] = 'inv'
            elif dataset.loc[i, 'reanimation'] < dataset.loc[
                                                    i + 1, 'reanimation']:
                dataset.loc[i, 'reanimation'] = dataset.loc[
                    i + 1, 'reanimation']
                dataset.loc[i + 1, 'reanimation'] = 'inv'

        if dataset.loc[i, 'maille_code'] == dataset.loc[
            i + 1, 'maille_code'] and dataset.loc[i, 'date'] == dataset.loc[
                i + 1, 'date'] and dataset.loc[i, 'hospitalises'] != 'inv':
            if pd.isnull(
                dataset.loc[i, 'hospitalises']) is True and pd.isnull(
                    dataset.loc[i + 1, 'hospitalises']) is False:
                    dataset.loc[i, 'hospitalises'] = dataset.loc[
                        i + 1, 'hospitalises']
                    dataset.loc[i + 1, 'hospitalises'] = 'inv'
            elif pd.isnull(
                    dataset.loc[i, 'hospitalises']) is False and pd.isnull(
                    dataset.loc[i + 1, 'hospitalises']) is True:
                dataset.loc[i + 1, 'hospitalises'] = 'inv'
            elif pd.isnull(
                    dataset.loc[i, 'hospitalises']) is True and pd.isnull(
                    dataset.loc[i + 1, 'hospitalises']) is True:
                        dataset.loc[i + 1, 'hospitalises'] = 'inv'
            elif dataset.loc[i, 'hospitalises'] == dataset.loc[
                                                    i + 1, 'hospitalises']:
                dataset.loc[i + 1, 'hospitalises'] = 'inv'
            elif dataset.loc[i, 'hospitalises'] > dataset.loc[
                                                    i + 1, 'hospitalises']:
                dataset.loc[i + 1, 'hospitalises'] = 'inv'
            elif dataset.loc[i, 'hospitalises'] < dataset.loc[
                                                    i + 1, 'hospitalises']:
                dataset.loc[i, 'hospitalises'] = dataset.loc[
                    i + 1, 'hospitalises']
                dataset.loc[i + 1, 'hospitalises'] = 'inv'

        if dataset.loc[i, 'maille_code'] == dataset.loc[
            i + 1, 'maille_code'] and dataset.loc[i, 'date'] == dataset.loc[
                i + 1, 'date'] and dataset.loc[i, 'gueris'] != 'inv':
            if pd.isnull(dataset.loc[i, 'gueris']) is True and pd.isnull(
                    dataset.loc[i + 1, 'gueris']) is False:
                dataset.loc[i, 'gueris'] = dataset.loc[i + 1, 'gueris']
                dataset.loc[i + 1, 'gueris'] = 'inv'
            elif pd.isnull(dataset.loc[i, 'gueris']) is False and pd.isnull(
                    dataset.loc[i + 1, 'gueris']) is True:
                dataset.loc[i + 1, 'gueris'] = 'inv'
            elif pd.isnull(dataset.loc[i, 'gueris']) is True and pd.isnull(
                    dataset.loc[i + 1, 'gueris']) is True:
                dataset.loc[i + 1, 'gueris'] = 'inv'
            elif dataset.loc[i, 'gueris'] == dataset.loc[i + 1, 'gueris']:
                dataset.loc[i + 1, 'gueris'] = 'inv'
            elif dataset.loc[i, 'gueris'] > dataset.loc[i + 1, 'gueris']:
                dataset.loc[i + 1, 'gueris'] = 'inv'
            elif dataset.loc[i, 'gueris'] < dataset.loc[i + 1, 'gueris']:
                dataset.loc[i, 'gueris'] = dataset.loc[i + 1, 'gueris']
                dataset.loc[i + 1, 'gueris'] = 'inv'

    # Delete the redundant resulting rows and reset the indices:
    dataset = dataset[dataset.cas_confirmes != 'inv']
    dataset = dataset.reset_index()
    dataset = dataset.drop(['index'], axis=1)

    # Rename/Translate the column titles:
    dataset = dataset.rename(
        columns={"maille_code": "subregion_code",
                 "maille_nom": "subregion_name", "cas_confirmes": "confirmed",
                 "deces": "deaths", "reanimation": "recovering",
                 "hospitalises": "hospitalized", "gueris": "recovered",
                 "source_nom": "source_name"})
    dataset['country'] = 'France'
    frcovidata = dataset[
        ['subregion_code', 'subregion_name', 'country', 'date', 'confirmed',
         'hospitalized', 'recovering', 'recovered',
         'deaths', 'source_name', 'source_url', 'source_archive',
         'source_type']]

    return frcovidata
