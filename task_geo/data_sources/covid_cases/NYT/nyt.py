import requests
import io
import pandas as pd
import numpy as np

def nyt_connector():
    """Retrieves data from The New York Time.

    Arguments:
        None

    Returns:
        pandas.DataFrame
    """
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    urlData = requests.get(url).content
    return pd.read_csv(io.StringIO(urlData.decode('utf-8')))


def nyt_formatter(raw):
    """Formats data retrieved from The New York Time.
    
    Arguments:
        raw(pandas.DataFrame):
    
    Returns:
        pandas.DataFrame
    """
    
    raw['country'] = "US"
    
    raw['date'] = pd.to_datetime(raw['date'].astype(str)).dt.date
    
    # convert fips read as float to string
    def format_fips(fips):
        if np.isnan(fips):
            return np.nan
        fips = str(int(fips))
        if len(fips) < 5:
            return "0" + fips
        return fips
    
    raw['fips'] = raw['fips'].apply(format_fips)
    
    rename = {
        'cases': 'cum_cases',
        'deaths': 'cum_deaths'
        }
    raw.rename(columns=rename, inplace=True)
    
    return raw[['country', 'state', 'county', 'fips', 'date', 'cum_cases',
                'cum_deaths']]


def us_covid_nyt():
    """Data source for US COVID-19 cases (per county), coming from The New York
    Times.

    Arguments:
        None

    Returns:
        pandas.DataFrame
    """
    data = nyt_connector()
    return nyt_formatter(data)