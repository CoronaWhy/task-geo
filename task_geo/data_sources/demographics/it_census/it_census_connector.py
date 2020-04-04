"""Retrieve data from Italian census.

Credits: http://demo.istat.it/index.html
License: http://creativecommons.org/licenses/by/3.0/it/

"""

from io import BytesIO
from zipfile import ZipFile

import pandas as pd
import requests

URL = 'http://demo.istat.it/pop2019/dati/comuni.zip'


def it_census_connector():
    zipped = requests.get(URL)
    zipdata = BytesIO(zipped.content)
    with ZipFile(zipdata) as content:
        data = pd.read_csv(content.open('comuni.csv'), skiprows=0, header=1)

    return data
