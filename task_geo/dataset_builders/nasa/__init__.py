from nasa.nasa_connector import nasa_connector
from nasa.nasa_formatter import nasa_formatter

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


def nasa(df, start_date, end_date=None,
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
