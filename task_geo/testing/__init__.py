import os

from task_geo.common.packaging import get_module_path
from task_geo.data_sources import execute_data_source, get_data_source

LOCATION_TERMS = ['city', 'sub_region', 'region', 'country']


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
    """Validate a dataset compliance of the Data Model.

    This validator will check for the following:
    - Column names are lower case.
    - Geopolitical division are corretly ordered.
    - Dates and timestamps use datetime dtype.
    - Numerical columns are not casted as objects.

    Arguments:
        data(pandas.DataFrame): output of data_source.

    Returns:
        None

    Raises:
        AssertionError: When some of the criteria are not meet.

    """
    message = 'All columns should be lowercase'
    assert all(data.columns == [column.lower() for column in data.columns]), message

    if 'latitude' in data.columns:
        message = 'Latitude should be provided with Longitude'
        assert 'longitude' in data.columns, message

    granularity = get_geographical_granularity(data)
    min_granularity_term = LOCATION_TERMS[granularity]

    locations = [data.columns.get_loc(LOCATION_TERMS[granularity])]
    for term in LOCATION_TERMS[granularity + 1:]:
        locations.append(check_column_and_get_index(term, data, min_granularity_term))

    message = 'The correct ordening of the columns is "country, region, sub_region, city"'
    assert (locations[::-1] == sorted(locations)), message

    message = 'date and timestamp columns should be of datetime dtype'
    time_index = None
    if 'date' in data.columns:
        assert data.date.dtype == 'datetime64[ns]', message
        time_index = data.columns.get_loc('date')

    if 'timestamp' in data.columns:
        assert data.timestamp.dtype == 'datetime64[ns]', message
        time_index = data.columns.get_loc('timestamp')

    if time_index is not None:
        message = 'geographical columns should be before time columns.'
        assert all(time_index > location for location in locations)

    object_columns = data.select_dtypes(include='object').columns

    for column in object_columns:
        try:
            data[column].astype(float)
            assert False, f'Column {column} is of dtype object, but casteable to float.'
        except ValueError:
            pass


def check_file_in_module(module_path, module_name, file_name):
    """Asserts that file_name is present in the given module.

    Arguments:
        module_path(str): Path to the module.
        module_name(str): Name of the module.
        file_name(str): File to check.

    Returns:
        None

    Raises:
        AssertiorEerror: If ``file_name`` is not a file in ``module_path``.
    """
    message = f'{file_name} is not present in datasource {module_name}'
    assert os.path.isfile(os.path.join(module_path, file_name)), message


def check_data_source_package(name, validate_output=False):
    """Checks the package formatting for a datasource.

    Arguments:
        name(str): Name of the data source.
        validate_output(bool): Flag for executing the datasource and evaluating its output.

    """
    data_source = get_data_source(name)

    module_path = get_module_path(data_source)
    check_file_in_module(module_path, data_source.__qualname__, 'audit.md')
    check_file_in_module(module_path, data_source.__qualname__, 'datapackage.json')

    if validate_output:
        output = execute_data_source(name)
        check_dataset_format(output)
