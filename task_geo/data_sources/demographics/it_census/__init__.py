from task_geo.data_sources.demographics.it_census.it_census_connector import it_census_connector
from task_geo.data_sources.demographics.it_census.it_census_formatter import it_census_formatter


def it_census():
    """Italian census data source.

    Arguments:
        None

    Returns:
        pandas.DataFrame

    Example:

    >>> from task_geo.data_sources import load_data_source
    >>> it_census = load_data_source('it_census')
    >>> data = it_census()
    """

    data = it_census_connector()
    return it_census_formatter(data)
