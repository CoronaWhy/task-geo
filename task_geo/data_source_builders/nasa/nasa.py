"""Extract meteorological data from NASA.

Source:
https://power.larc.nasa.gov/
"""
import itertools
import pandas as pd
import requests


PARAMETERS = {
    "temperature": ["T2M", "T2M_MIN", "T2M_MAX"],
    "humidity": ["RH2M", "QV2M"],
    "pressure": ["PS"]
}

COL_NAMES = {
    "T2M": "avg_temperature",
    "T2M_MIN": "min_temperature",
    "T2M_MAX": "max_temperature",
    "RH2M": "relative_humidity",
    "QV2M": "specific_humidity",
    "PS": "pressure"
}


def nasa_data_loc(lat, lon, str_start_date, str_end_date, parms_str):
    """
    Extract data for a single location.

    Parameters
    ----------
    lat : string
    lon : string
    str_start_date : string
    str_end_date : string
    parms_str : string

    Returns
    -------
    df : pandas.DataFrame

    """
    base_url = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py"

    identifier = "identifier=SinglePoint"
    user_community = "userCommunity=SSE"
    temporal_average = "tempAverage=DAILY"
    output_format = "outputList=JSON,ASCII"
    user = "user=anonymous"

    url = f"{base_url}?request=execute&{identifier}&{parms_str}&" \
          f"startDate={str_start_date}&endDate={str_end_date}&" \
          f"lat={lat}&lon={lon}&{temporal_average}&{output_format}&" \
          f"{user_community}&{user}"
    response = requests.get(url)
    data_json = response.json()
    df = pd.DataFrame(data_json['features'][0]['properties']['parameter'])
    df['lon'] = lon
    df['lat'] = lat
    return df


def nasa_connector(df_locations, start_date, end_date=None,
                   parms=None):
    """
    Retrieve meteorologic data from NASA.

    Given a dataset with columns country, region, sub_region, lon, and lat, for
    each geographic coordinate (lon, lat) corresponding to a place (specified
    if country, region, or sub_region) extract the time series of the desired
    data at the location.

    Arguments:
    ---------
        df_locations(pandas.DataFrame): Dataset with columns lon, and lat
        start_date(datetime): Start date for the time series
        end_date(datetime): End date for the time series (optional)
        parms(list of strings): Desired data, accepted are 'temperature',
                                'humidity', and 'pressure' (optional)

    Return:
    ------
        pandas.DataFrame:   Columns are country, region, sub_region (non-null),
                            lon, lat, date, and the desired data.
    """
    if parms is None:
        parms = list(PARAMETERS.keys())

    df_locations = df_locations[
        ~pd.isna(df_locations[['lon', 'lat']]).all(axis=1)
    ]
    location_data = ['country', 'region', 'sub_region', 'lon', 'lat']
    locations = df_locations[location_data].drop_duplicates()

    str_start_date = str(start_date.date()).replace('-', '')

    if end_date is None:
        str_end_date = str(pd.Timestamp.today().date()).replace('-', '')
    else:
        str_end_date = str(end_date.date()).replace('-', '')

    all_parms = list(itertools.chain.from_iterable([PARAMETERS[p]
                                                    for p in parms]))
    parms_str = f"parameters={','.join(all_parms)}"

    return pd.concat([
        nasa_data_loc(row.lat, row.lon, str_start_date, str_end_date,
                      parms_str)
        for row in locations.itertuples()
    ])


def nasa_formatter(df_nasa, parms):
    """
    Format the NASA data.

    Parameters
    ----------
    df_nasa : pandas.DataFrame
    parms : list of strings

    Returns
    -------
    df_nasa : pandas.DataFrame

    """
    # date column
    df_nasa.reset_index(inplace=True, drop=False)
    df_nasa.rename(columns={'index': 'date'}, inplace=True)
    df_nasa['date'] = pd.to_datetime(df_nasa['date'], format='%Y%m%d')

    # reorder columns
    base_parms = ['lon', 'lat', 'date']
    all_parms = list(itertools.chain.from_iterable([PARAMETERS[p]
                                                    for p in parms]))
    df_nasa = df_nasa[base_parms + all_parms]

    # rename columns
    df_nasa.rename(columns=COL_NAMES, inplace=True)

    return df_nasa


def nasa_meteo_data(df, start_date, end_date=None,
                    parms=None, join=True):
    """
    Retrieve meteorologic data from NASA.

    Given a dataset with columns country, region, sub_region, lon, and lat, for
    each geographic coordinate (lon, lat) corresponding to a place (specified
    if country, region, or sub_region) extract the time series of the desired
    data at the location.

    Arguments:
    ---------
        df(pandas.DataFrame): Dataset with columns lon, and lat
        start_date(datetime): Start date for the time series
        end_date(datetime): End date fo rthe time series (optional)
        parms(list of strings): Desired data, accepted are 'temperature',
                                'humidity', and 'pressure' (optional)
                                Defaults to all.
        join(bool): Determine if the meteorologic data has to be joined to the
                    original dataset

    Return:
    ------
        pandas.DataFrame:   Columns are lon, lat, date, and the desired data,
                            plus the columns of the original dataframe if
                            join=True.

    """
    if parms is None:
        parms = list(PARAMETERS.keys())

    df_nasa = nasa_connector(df, start_date, end_date=end_date,
                             parms=parms)
    if not join:
        return nasa_formatter(df_nasa, parms)
    else:
        return df.merge(
            nasa_formatter(df_nasa, parms),
            how='left', on=['lon', 'lat']
        )
