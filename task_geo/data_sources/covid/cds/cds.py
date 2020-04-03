""" Source of Data: https://coronadatascraper.com/#timeseries.json """

import pandas as pd


def cds_connector(country=None):
    """Retrieve data from Corona Data Scraper.

    This connector has two ways of working:
    - When given the country it will return a pandas.DataFrame with the data for the given country.
    - When no argument is given, returns the raw data.

    Arguments:
        country[str]: 3 letter ISO country code.Optional

    Returns:
        pandas.DataFrame
    """
    df = pd.read_csv("https://coronadatascraper.com/timeseries.csv")
    return df if country is None else df[df['country'] == country]


def cds_formatter(df):
    """Formats data from CoronaDataScraper.
    Arguments:
        df(pandas.DataFrame): Raw data returned from cds_connector.

    Returns:
        pandas.DataFrame
    """

    assert df[pd.isnull(df.country)].empty

    df = df.rename(columns={'growthFactor': 'growth_factor'})
    df = df.reindex(columns=[
        'city', 'county', 'state', 'country', 'population', 'lat', 'long',
        'date', 'url', 'aggregate', 'tz', 'cases', 'deaths', 'recovered',
        'active', 'tested', 'growth_factor'
    ])
    df['date'] = pd.to_datetime(df.date)

    return df.sort_values(by='date').reset_index(drop=True)


def cds_datasource(country=None):
    """CoronaDataScraper Data Source.

    This data source has two ways of working:
    - When given the country it will return a pandas.DataFrame with the data for the given country.
    - When no argument is given, returns the raw data.

    Arguments:
        country[str]: 3 letter ISO country code.Optional

    Returns:
        pandas.DataFrame
    """
    data = cds_connector(country)

    return cds_formatter(data)
