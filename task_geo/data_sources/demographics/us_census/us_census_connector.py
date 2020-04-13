import urllib.request
import zipfile

import pandas as pd

url = 'https://data.census.gov/api/access/table/download?download_id=iuGrLXEBm-bIwvlxENnx'


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
