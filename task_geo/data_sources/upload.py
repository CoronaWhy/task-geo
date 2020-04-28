"""Functions and helpers to automate the execution and uploading of datasources."""
import json
import logging
import os
import shutil
from datetime import datetime

from kaggle_storage_client import KaggleStorageClient

from task_geo.common.packaging import get_module_path
from task_geo.data_sources import (
    AVAILABLE_DATA_SOURCES, execute_data_source, get_data_source, get_update_policy)
from task_geo.testing import check_data_source_package

LOGGER = logging.getLogger(__name__)


class StorageClient:

    def __init__(self, *args, **kwargs):
        pass

    def upload(self, path, *args, **kwargs):
        """Upload the contents of given path to the storage.

        Arguments:
            path(str): Path to upload

        """
        pass

    def check(self, file_path):
        """Check if given file exist in the storage and returns its timestamp."""
        pass


class Kaggle(StorageClient):

    def __init__(self):
        self.client = KaggleStorageClient(datadir='task-geo-datasets', login_file=False)

    def upload(self, path):
        dataset = os.path.dirname(path)
        for file_name in os.listdir(path):
            self.client.upload(dataset, os.path.join(path, file_name))


class GCloud(StorageClient):
    pass


class DataVerse(StorageClient):
    """Dataverse integration client. """
    pass


STORAGE_CLIENTS = {
    'kaggle': Kaggle,
    'gcloud': GCloud,
}


def update_datapackage(json_path, dataset_name, timestamp):
    """Updates the metapackage.json with timestamp.

    Arguments:
        json_path(str): Path to the datapackage.json to modify.
        dataset_name(str): File name of the dataset.
        timestamp(datetime): Timestamp.

    Return:
        None

    """
    with open(json_path, 'r+') as f:
        metadata = json.load(f)
        metadata['id'] = (
            f'coronawhy/task-geo/{dataset_name[:-4]}_{timestamp.strftime("%Y%m%d%H%M%S%f")}')
        metadata['timestamp'] = timestamp.isoformat()
        metadata['resources'][0]['path'] = dataset_name
        metadata['resources'].append({
            'path': 'audit.md',
            'description': 'Contains detailed information about the dataset.'
        })

        f.seek(0)
        json.dump(metadata, f, indent=4)


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

    name = name.replace('_', '-')
    dataset = execute_data_source(name)
    timestamp = datetime.now()

    folder_path = os.path.join(path, name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

    os.makedirs(folder_path)

    dataset_name = f'{name}.csv'
    dataset_path = os.path.join(folder_path, dataset_name)
    dataset.to_csv(dataset_path, index=False, header=True)

    module_path = get_module_path(get_data_source(name))

    json_path = os.path.join(folder_path, 'dataset-metadata.json')
    shutil.copy(os.path.join(module_path, 'datapackage.json'), json_path)
    shutil.copy(os.path.join(module_path, 'audit.md'), folder_path)

    update_datapackage(json_path, dataset_name, timestamp)

    return folder_path


def updated_data_source(name):
    """Check if a dataset should be updated.

    The check is done following this rules:
    1. If the data_source is marked as `update`(1), will return True.
    2. If the data_source is not marked as `update`(1), but there is no dataset uploaded,
    will return True.
    3. If the data_source is not marked as `update`(1), there is a dataset uploaded, but the data
    source has been changed since the dataset was generated, return True.

    In any other case, will return False.

    (1) Marked as such in DATA_SOURCE_DEFAULT_PARAMETERS

    Arguments:
        name(str): Data source name.

    Returns:
        bool.

    """
    return get_update_policy(name)


def process_datasets(storage='dataverse'):
    if storage is not None:
        client = STORAGE_CLIENTS[storage]()
    else:
        client = None

    if storage == 'kaggle':
        path = os.path.join('task-geo-datasets', os.environ['KAGGLE_USERNAME'])
    else:
        path = 'task-geo-datasets'

    for name in AVAILABLE_DATA_SOURCES:
        LOGGER.info('Preparing to process data source %s', name)
        try:
            check_data_source_package(name)
            valid_package = True
        except AssertionError:
            valid_package = False
            LOGGER.info('Invalid module format, skipping...')

        if valid_package and updated_data_source(name):
            LOGGER.info('Executing data source %s', name)
            folder_path = prepare_data_package(name, path=path)

            LOGGER.info('Uploading generated dataset to %s', storage)
            client.upload(folder_path)
