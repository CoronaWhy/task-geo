import pandas as pd

from task_geo.common.country_codes import iso_to_name


def mobility_formatter(raw):
    # Put column names in lowercase alphanumerical
    columns = ['_'.join(column.replace(' & ', '_').lower().split(' ')) for column in raw.columns]
    raw.columns = columns
    raw['country'] = raw.country_iso.apply(iso_to_name)

    numeric_columns = [
        'retail_recreation', 'grocery_pharmacy', 'parks',
        'transit_stations', 'workplaces', 'residential'
    ]
    raw[numeric_columns] = raw[numeric_columns].astype(float)
    raw['date'] = pd.to_datetime(raw.date)
    column_order = [
        'country_iso', 'country', 'region', 'date', 'retail_recreation', 'grocery_pharmacy',
        'parks', 'transit_stations', 'workplaces', 'residential'
    ]
    return raw[column_order]
