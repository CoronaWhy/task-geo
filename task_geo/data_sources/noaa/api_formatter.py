import pandas as pd

from task_geo.common.country_codes import fips_to_name
from task_geo.data_sources.noaa.api_connector import DEFAULT_METRICS


def noaa_api_formatter(raw, metrics=None):
    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]

    if metrics is None:
        metrics = [metric.lower() for metric in DEFAULT_METRICS if metric in raw.columns]

    column_order = [
        'latitude', 'longitude', 'elevation', 'country', 'name',
        'date', 'station']
    column_order.extend(metrics)

    data.date = pd.to_datetime(data.date)

    for column in ['tmax', 'tavg', 'tmin']:
        if column in raw.columns:
            data.loc[:, column] = data[column].astype(float) / 10

    if 'snwd' in raw.columns:
        data.loc[:, 'snwd'] = data['snwd'].astype(float) / 1000
        data.snwd.fillna(0, inplace=True)

    if 'prcp' in raw.columns:
        data.loc[:, 'prcp'] = data['prcp'].astype(float) / 10000

    data['country'] = data.station.str.slice(0, 2).apply(fips_to_name)

    return data[column_order]
