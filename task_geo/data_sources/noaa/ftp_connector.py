"""Extract and prepare meteorological data from https://www.ncdc.noaa.gov/
the National Centers for Environmental Information

Credits for the data:

Menne, M.J., I. Durre, B. Korzeniewski, S. McNeal, K. Thomas, X. Yin, S. Anthony, R. Ray,
R.S. Vose, B.E.Gleason, and T.G. Houston, 2012: Global Historical Climatology Network -
Daily (GHCN-Daily), Version 3. [indicate subset used following decimal,
e.g. Version 3.12].
NOAA National Climatic Data Center. http://doi.org/10.7289/V5D21VHZ [2020].
"""

import logging
import os
import re
import tarfile as tar
from datetime import datetime
from ftplib import FTP

import pandas as pd

from task_geo.data_sources.noaa.references import DATA_DIRECTORY, load_dataset

logging.basicConfig(level=logging.DEBUG)


NOAA_FTP_FILES = {
    'readme.txt': 'RETR readme.txt',
    'stations_metadata.txt': 'RETR ghcnd-stations.txt',
    'country_codes.txt': 'RETR ghcnd-countries.txt',
    'stations_inventory.txt': 'RETR ghcnd-inventory.txt',
    'all_daily_data.tar.gz': 'RETR ghcnd_all.tar.gz'
}

INDEX_COLUMNS = [
    'ID',
    'YEAR',
    'MONTH',
    'ELEMENT'
]
REGEX = re.compile(r'^(\w*?)(\d+)$')


def download_noaa_files(large_files=True, skip_downloaded=False):
    """Download files from the NOAA FTP server.

    Arguments:
        large_files(bool):
            Wheter or not to download the 3Gb daily reports, only download reference data.
        skip_downloaded(bool):
            Check if the file exists on local and has the same size that in the server,
            if True, will be skiped, if False will download it.

    Returns:
        None. The files will be downloaded on DOWNLOADED_DIRECTORY.
    """
    logging.info('Connecting to NOAA FTP server.')
    ftp = FTP('ftp.ncdc.noaa.gov')
    ftp.login()

    ftp.cwd('/pub/data/ghcn/daily/')

    for filename, action in NOAA_FTP_FILES.items():

        if filename.endswith('tar.gz'):
            if not large_files:
                continue

            logging.debug('This is file is more than 3Gb+, it may take a long time.')

        logging.debug('Downloading %s', filename)

        path = os.path.join(DATA_DIRECTORY, filename)

        if not os.path.exists(path) and not os.path.isdir(DATA_DIRECTORY):
            os.mkdir(DATA_DIRECTORY)

        if skip_downloaded:
            server_file_name = action.split(' ')[1]
            if os.path.exists(path) and ftp.size(server_file_name) == os.stat(path).st_size:
                continue

        with open(path, 'wb') as fp:
            ftp.retrbinary(action, fp.write)

    if large_files:
        logging.debug('Extracting daily data.')
        tar_path = f'{DATA_DIRECTORY}/all_daily_data.tar.gz'
        with tar.open(tar_path) as tar_all:
            tar_all.extractall(path=f'{DATA_DIRECTORY}/all_daily/')

    logging.debug('Done!')


def to_date(row):
    try:
        return datetime(row['YEAR'], row['MONTH'], row['DAY'])
    except ValueError:
        return None


def load_and_filter_dataset(dataset_name):
    dataset = load_dataset(dataset_name)
    return dataset[(dataset.YEAR >= 2020) | ((dataset.YEAR == 2019) & (dataset.MONTH >= 11))]


def load_stations_data(station_ids):
    stations_data = pd.concat([
        load_and_filter_dataset(station_id)
        for station_id in station_ids
    ]).set_index(INDEX_COLUMNS)

    stacked = stations_data.stack().reset_index(level=-1)
    stacked.columns = ['name', 'value']

    column_day = stacked.name.str.extract(REGEX)
    stacked['column'] = column_day[0]
    stacked['DAY'] = column_day[1].astype(int)
    del stacked['name']

    values = stacked.set_index(['DAY', 'column'], append=True)

    unstacked = values.unstack(level=-1)
    unstacked.columns = unstacked.columns.droplevel(0)
    unstacked.reset_index(inplace=True)
    unstacked.columns = list(unstacked.columns)

    unstacked['DATE'] = unstacked.apply(to_date, axis=1)
    unstacked.drop(labels=['YEAR', 'MONTH', 'DAY'], axis=1, inplace=True)

    return unstacked.dropna(subset=['DATE'])


def process_noaa_files(countries):
    """Returns a dataset for the given countries.

    Arguments:
        countries(list[str]): List of countries in ISO-2 format.

    Returns:
        pandas.DataFrame
    """

    df_stations = load_dataset('stations')
    df_countries = load_dataset('countries')

    # Join country to df_stations
    df_stations['COUNTRY_CODE'] = df_stations['ID'].str.slice(0, 2)
    df_stations = df_stations.merge(df_countries, on=['COUNTRY_CODE'], how='left')

    df_stations = df_stations[df_stations['COUNTRY_CODE'].isin(countries)]

    df_daily_information = load_stations_data(df_stations['ID'])

    return df_daily_information.merge(df_stations, how='left', on=['ID'])


def noaa_ftp_connector(countries, download=True):
    """Retrieves data from the NOAA FTP server.

    Arguments:
        countries(list[str]):
            List of countries in ISO-2 format.

        download(bool):
            Wheter or not to download the data, and just process previously downloaded data.
    """
    if download:
        download_noaa_files()

    return process_noaa_files(countries)
