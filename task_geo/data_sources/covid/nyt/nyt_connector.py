import pandas as pd


def nyt_connector():
    """Retrieves data from The New York Times.

    Arguments:
        None

    Returns:
        pandas.DataFrame
    """
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    return pd.read_csv(url)
