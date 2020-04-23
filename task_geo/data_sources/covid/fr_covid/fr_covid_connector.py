import io

import pandas as pd
import requests

url = (
    'https://raw.githubusercontent.com/opencovid19-fr/'
    'data/master/dist/chiffres-cles.csv'
)


def fr_covid_connector():
    """Extract data from OpenCOVID19-fr's Github repository.

    Description:
        - Downloads the URL's data in a Unicode CSV Format
        - Unicode CSV Format: ACS 5Y UTF-8

    Arguments:
        None

    Returns:
        dataset (DataFrame with CSV Data)

    """
    urlData = requests.get(url).content

    return pd.read_csv(io.StringIO(urlData.decode('utf-8')))
