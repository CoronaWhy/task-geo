from datetime import datetime

from task_geo.data_sources.covid.cds import cds
from task_geo.data_sources.covid.nyt import nyt
from task_geo.data_sources.demographics.us_census import us_census
from task_geo.data_sources.hdx_acap import hdx_acap
from task_geo.data_sources.noaa import noaa_api

AVAILABLE_DATA_SOURCES = {
    'noaa_api': noaa_api,
    'cds': cds,
    'us_census': us_census,
    'nyt': nyt,
    'hdx_acap': hdx_acap
}

COUNTRIES = ['FR']
START_DATE = datetime(2019, 11, 15)


DATA_SOURCE_DEFAULT_PARAMETERS = {
    'noaa_api': {
        'args': [COUNTRIES, START_DATE],
        'kwargs': {},
        'update': True
    },
    'cds': {
        'args': [],
        'kwargs': {},
        'update': True
    },
    'us_census': {
        'args': [],
        'kwargs': {},
        'update': False
    },
    'nyt': {
        'args': [],
        'kwargs': {},
        'update': True
    },
    'hdx_acap': {
        'args': [],
        'kwargs': {},
        'update': True
    },
}


def list_data_sources():
    """List all available data sources."""
    return list(AVAILABLE_DATA_SOURCES.keys())


def show_data_source_docs(data_source):
    """Prints the docs of the requested data source."""
    print(AVAILABLE_DATA_SOURCES[data_source].__doc__)


def get_data_source(data_source):
    """Return the requested data source."""
    return AVAILABLE_DATA_SOURCES[data_source]


def get_default_parameters(name):
    """Return the default parameters for a data source.

    Arguments:
        name(str): Name of the data source.

    Returns:
        tuple[list, dict]
    """
    node = DATA_SOURCE_DEFAULT_PARAMETERS[name]
    return node['args'], node['kwargs']


def get_update_policy(name):
    return DATA_SOURCE_DEFAULT_PARAMETERS[name]['update']


def execute_data_source(name):
    """Finds a datasource by it's name and executes it with their default parameters.

    Arguments:
        name(str): Name of the data source.
    """
    data_source = get_data_source(name)
    args, kwargs = get_default_parameters(name)

    return data_source(*args, **kwargs)
