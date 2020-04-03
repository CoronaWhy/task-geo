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
