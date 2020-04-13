import numpy as np
import pandas as pd


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

    return raw[['country', 'state', 'county', 'fips', 'date', 'cum_cases', 'cum_deaths']]
