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

"""
us_census
Method for combining the connector and formatter functions

Returns:
    finalized data (Cleaned DataFrame)

"""


def us_census():
    df = us_census_connector()
    return us_census_formatter(df)


"""
us_census_connector
Method for extracting data from the US Census CSV URL

Description:
    - Opens the zip file URL and extracts the correct CSV
    - Correct CSV: ACS 5Y Statistics

Returns:
    data (DataFrame with CSV Data)

"""


def us_census_connector():

    urllib.request.urlretrieve(url, "uscensus.zip")

    with zipfile.ZipFile("uscensus.zip") as myzip:

        listFiles = myzip.namelist()

        myzip.extract(listFiles[5])
        data = pd.read_csv(listFiles[5], low_memory=False)

    return data


"""
us_census_formatter
Method for filtering out unwanted census statistics and formatting columns

Description:
    - Drop unnecessary columns and set index to county
    - Make column values more readable

Returns: Cleaned Pandas DataFrame

"""


def us_census_formatter(data):

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
