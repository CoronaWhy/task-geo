""" Source of Data: https://coronadatascraper.com/#timeseries.json """

import pandas as pd


def cds_connector(country=None):
    """
      Input:  Accept country value in 3 digit format
      Output: Return raw dataframe of all countries
    """
    df = pd.read_csv("https://coronadatascraper.com/timeseries.csv")
    return df if country is None else df[df['country'] == country]


def cds_formatter(df):
    """
      Input:  Raw data from Connector
      Output: Return data frame of the specified country
    """

    assert df[pd.isnull(df.country)].empty

    df = df.rename(columns={'growthFactor': 'growth_factor'})
    df = df.reindex(columns=['city', 'county', 'state', 'country', 'population', 'lat', 'long',
                             'date', 'url', 'aggregate', 'tz', 'cases', 'deaths', 'recovered',
                             'active', 'tested', 'growth_factor'])
    df['date'] = pd.to_datetime(df.date)

    return df.sort_values(by='date').reset_index(drop=True)


def cds_datasource(country=None):
    """
      Input:  Accept Country name as 3 digit code
      Output: Return formatted dataframe of all countries
    """
    data = cds_connector(country)

    return cds_formatter(data)
