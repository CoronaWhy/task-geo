import os

DTYPES_NAME = {
    'float64': 'float',
    'int64': 'int',
    'datetime64[ns]': 'datetime',
    'object': 'string'
}


def get_module_path(function):
    """Return the path to the module of a function.

    Argument:
        function(callable): Function to retrieve the module path from.

    Returns:
        str

    """
    return os.path.join(*function.__module__.split('.'))


def generate_datapackage_json(data, name):
    """Generate a basic datapackage.json using the data.

    Arguments:
        data(pandas.DataFrame): Output from the data source.
        name(str): Name of the data source.

    Returns:
        dict
    """

    metadata = {
        'subtitle': 'xxxx',
        'description': 'xxxx',
        'resources': [{
            'description': 'xxxx',
            'schema': {
                'fields': [],
            }
        }],
        'keywords': ['coronawhy', name]
    }

    for column, dtype in data.dtypes.items():
        metadata['resources'][0]['schema']['fields'].append(
            {
                'name': column,
                'description': 'xxxx',
                'type': DTYPES_NAME.get(str(dtype))
            }
        )

    return metadata
