"""Functions and helpers to automate the execution and uploading of datasources."""
import json
import os
import shutil
from datetime import datetime

from task_geo.common.packaging import get_module_path
from task_geo.data_sources import get_data_source

COUNTRIES = ['FR']
START_DATE = datetime(2019, 11, 15)


DATA_SOURCE_DEFAULT_PARAMETERS = {
    'noaa_api': {
        'args': [COUNTRIES, START_DATE],
        'kwargs': {},
    },
    'cds': {
        'args': [],
        'kwargs': {}
    },
    'us_census': {
        'args': [],
        'kwargs': {}
    },
    'nyt': {
        'args': [],
        'kwargs': {}
    },
    'hdx_acap': {
        'args': [],
        'kwargs': {}
    },
}


def get_default_parameters(name):
    """Return the default parameters for a data source.

    Arguments:
        name(str): Name of the data source.

    Returns:
        tuple[list, dict]
    """
    node = DATA_SOURCE_DEFAULT_PARAMETERS[name]
    return node['args'], node['kwargs']


def execute_data_source(name):
    """Finds a datasource by it's name and executes it with their default parameters.

    Arguments:
        name(str): Name of the data source.
    """
    data_source = get_data_source(name)
    args, kwargs = get_default_parameters(name)

    return data_source(*args, **kwargs)


def update_datapackage_json(json_path, dataset_name, timestamp):
    """Updates the metapackage.json with timestamp.

    Arguments:
        json_path(str): Path to the datapackage.json to modify.
        dataset_name(str): File name of the dataset.
        timestamp(datetime): Timestamp.

    Return:
        None

    """
    with open(json_path) as f:
        metadata = json.load(f)

    metadata['id'] = f'coronawhy/task-geo/{dataset_name[:-4]}'
    metadata['timestamp'] = timestamp.isoformat()
    metadata['resources'][0]['path'] = dataset_name
    metadata['resources'].append({
        'path': 'audit.md',
        'description': 'Contains detailed information about the dataset.'
    })

    with open(json_path, 'w') as f:
        json.dump(metadata, f)

    return


def prepare_data_package(name, path=None):
    """Runs a data source and prepare everything to upload to a cloud storage.

    This functions will:
    - Create a subfolder with path ``path``/``name`` if it doesn't exist.
    - Remove all existing files in that folder if it already existed.
    - Import the data source using ``get_data`` and execute it using the default parameters.
    - Copy both audit.md and datapackage.json

    Arguments:
        name(str): Name of the data source.
        path(Union[None, str]): Either a valid folder, or None to use the current directory.

    Returns:
        str: Path to the generated folder.

    """
    if path is None:
        path = os.getcwd()

    folder_path = os.path.join(path, name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

    os.mkdirs(folder_path)

    dataset = execute_data_source(name)
    timestamp = datetime.now()

    dataset_name = f'{name}_{timestamp.strftime("%Y%m%d%H%M%S%f")}.csv'
    dataset_path = os.path.join(folder_path, dataset_name)
    dataset.to_csv(dataset_path, index=False, header=True)

    module_path = get_module_path(get_data_source(name))

    json_path = os.path.join(module_path, 'datapackage.json')
    shutil.copy(json_path, folder_path)
    shutil.copy(os.path.join(module_path, 'audit.md'), folder_path)

    update_datapackage_json(json_path, dataset_name, timestamp)

    return folder_path
