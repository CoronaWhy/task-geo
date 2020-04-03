"""
us_census.py

Functions:
    - us_census_connector: Extracts data from CSV URL
    - us_census_formatter: Cleans CSV data
    - us_census: Combines the two previous functions

Data Credits:
    The United States Census Bureau
    https://data.census.gov/
"""

import urllib.request
import zipfile

import pandas as pd

url = 'https://data.census.gov/api/access/table/download?download_id=iuGrLXEBm-bIwvlxENnx'


def us_census():
    """Data Source for the US census.

    Arguments:
        None

    Returns:
        pandas.DataFrame
    """
    df = us_census_connector()
    return us_census_formatter(df)


def us_census_connector():
    """Extract data from the US Census.


    Description:
        - Opens the zip file URL and extracts the correct CSV
        - Correct CSV: ACS 5Y Statistics

    Returns:
        data (DataFrame with CSV Data)
    """

    urllib.request.urlretrieve(url, "uscensus.zip")

    with zipfile.ZipFile("uscensus.zip") as myzip:

        listFiles = myzip.namelist()

        myzip.extract(listFiles[5])
        data = pd.read_csv(listFiles[5], low_memory=False)

    return data


def us_census_formatter(data):
    """Formatter for US Census.

    Arguments:
        data(pandas.DataFrame): Data as returned by us_census_connector.

    Description:
        - Drop unnecessary columns and set index to county
        - Make column values more readable

    Returns:
        pandas.DataFrame
    """

    data.columns = data.iloc[0]
    data.drop(0, inplace=True)
    data.drop("id", axis=1, inplace=True)
    data = data.set_index('Geographic Area Name')

    cols = [c for c in data.columns if '2018' in c]
    data = data[cols]
    data.columns = [x.split("!!")[-1] for x in data.columns]

    data = data.replace("N", 0.0)
    data.columns = [x.lower() for x in data.columns]

    data.drop(data.columns[-1], axis=1, inplace=True)
    data.drop(data.columns[-1], axis=1, inplace=True)

    return data
