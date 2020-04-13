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


def list_data_sources():
    """List all available data sources."""
    return list(AVAILABLE_DATA_SOURCES.keys())


def show_data_source_docs(data_source):
    """Prints the docs of the requested data source."""
    print(AVAILABLE_DATA_SOURCES[data_source].__doc__)


def get_data_source(data_source):
    """Return the requested data source."""
    return AVAILABLE_DATA_SOURCES[data_source]
