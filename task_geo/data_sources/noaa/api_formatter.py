import pandas as pd

from task_geo.common.country_codes import fips_to_name
from task_geo.data_sources.noaa.api_connector import DEFAULT_METRICS


def noaa_api_formatter(raw, metrics=None, country_avg=False):
    """Format the output of the NOAA API to the task-geo Data Model.

    Arguments:
        raw(pandas.DataFrame):Data to be formatted.
        metrics(list[str]): Optional.List of metrics requested,valid metric values are:
            TMIN: Minimum temperature.
            TMAX: Maximum temperature.
            TAVG: Average of temperature.
            SNOW: Snowfall (mm).
            SNWD: Snow depth (mm).
        country_avg(bool): When True, only an average for each date/country will be returned.

    Returns:
        pandas.DataFrame

    """
    if metrics is None:
        metrics = [metric.lower() for metric in DEFAULT_METRICS if metric in raw.columns]

    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]

    column_order = [
        'latitude', 'longitude', 'elevation', 'country', 'name',
        'date', 'station']
    column_order.extend(metrics)

    data.date = pd.to_datetime(data.date)

    for column in ['tmax', 'tavg', 'tmin']:
        if column in data.columns:
            data[column] = data[column].astype(float) / 10

    if 'snwd' in data.columns:
        data['snwd'] = data['snwd'].astype(float) / 1000
        data.snwd.fillna(0, inplace=True)

    if 'prcp' in data.columns:
        data['prcp'] = data['prcp'].astype(float) / 10000

    data['country'] = data.station.str.slice(0, 2).apply(fips_to_name)
    data = data[column_order]

    if country_avg:
        return data.groupby(['country', 'date'])[metrics].mean().reset_index()

    return data
