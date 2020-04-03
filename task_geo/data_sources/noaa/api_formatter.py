import pandas as pd

from task_geo.common.country_codes import fips_to_name


def noaa_api_formatter(raw):
    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]

    column_order = [
        'latitude', 'longitude', 'elevation', 'country', 'name',
        'date', 'station', 'tmax', 'tavg', 'tmin', 'prcp', 'snwd']

    data.date = pd.to_datetime(data.date)

    for column in ['tmax', 'tavg', 'tmin']:
        data.loc[:, column] = data[column].astype(float) / 10

    data.loc[:, 'snwd'] = data['snwd'].astype(float) / 1000
    data.snwd.fillna(0, inplace=True)

    data.loc[:, 'prcp'] = data['prcp'].astype(float) / 10000
    data['country'] = data.station.str.slice(0, 2).apply(fips_to_name)

    return data[column_order]
