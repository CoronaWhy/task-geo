import numpy as np
import pandas as pd

from task_geo.common.country_codes import fips_to_name
from task_geo.data_sources.noaa.noaa_api_connector import DEFAULT_METRICS


def noaa_api_formatter(raw, metrics=None, country_aggr=False):
    """Format the output of the NOAA API to the task-geo Data Model.

    Arguments:
        raw(pandas.DataFrame):Data to be formatted.
        metrics(list[str]): Optional.List of metrics requested,valid metric values are:
            TMIN: Minimum temperature.
            TMAX: Maximum temperature.
            TAVG: Average of temperature.
            SNOW: Snowfall (mm).
            SNWD: Snow depth (mm).
            PRCP: Precipitation
        country_aggr(bool): When True, only an aggregate for each date/country will be returned.

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
            data[column] = data[column].astype(float)

    if 'snwd' in data.columns:
        data['snwd'] = data['snwd'].astype(float) / 1000
        data.snwd.fillna(0, inplace=True)

    if 'prcp' in data.columns:
        data['prcp'] = data['prcp'].astype(float) / 1000
        data.prcp.fillna(0, inplace=True)

    data['country'] = data.station.str.slice(0, 2).apply(fips_to_name)
    data = data[column_order]

    if country_aggr:
        aggregations = {}
        if 'tmin' in metrics:
            aggregations['tmin'] = np.min

        if 'tmax' in metrics:
            aggregations['tmax'] = np.max

        agg_columns = list(aggregations.keys())
        return data.groupby(['country', 'date'])[agg_columns].aggregate(aggregations).reset_index()

    return data
