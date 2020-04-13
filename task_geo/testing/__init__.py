LOCATION_TERMS = ['city', 'subregion', 'region', 'country']


def get_geographical_granularity(data):
    """Returns the index of the lowest granularity level available in data."""
    for index, term in enumerate(LOCATION_TERMS):
        if term in data.columns:
            return index


def check_column_and_get_index(name, data, reference):
    """Check that name is present in data.columns and returns it's index."""
    assert name in data.columns, f'If {reference} is provided, {name} should be present too'
    return data.columns.get_loc(name)


def check_dataset_format(data):

    message = 'All columns should be lowercase'
    assert all(data.columns == [column.lower() for column in data.columns]), message

    if 'latitude' in data.columns:
        message = 'Latitude should be provided with Longitude'
        assert 'longitude' in data.columns, message

    granularity = get_geographical_granularity(data)
    if granularity is not None:
        min_granularity_term = LOCATION_TERMS[granularity]

        locations = [granularity]
        for term in LOCATION_TERMS[granularity + 1:]:
            locations.append(check_column_and_get_index(term, data, min_granularity_term))

        message = 'The correct ordening of the columns is "country, region, sub_region, city"'
        assert (locations == sorted(locations)), message

    message = 'date and timestamp columns should be of datetime dtype'
    time_index = None
    if 'date' in data.columns:
        assert data.date.dtype == 'datetime64[ns]', message
        time_index = data.columns.get_loc('date')

    if 'timestamp' in data.columns:
        assert data.timestamp.dtype == 'datetime64[ns]', message
        time_index = data.columns.get_loc('timestamp')

    if time_index is not None and granularity is not None:
        message = 'geographical columns should be before time columns.'
        assert all(time_index > location for location in locations)

    object_columns = data.select_dtypes(include='object').columns

    for column in object_columns:
        try:
            data[column].astype(float)
            assert False, f'Column {column} is of dtype object, but casteable to float.'
        except ValueError:
            pass
