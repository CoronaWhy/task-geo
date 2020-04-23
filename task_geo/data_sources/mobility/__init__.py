from task_geo.data_sources.mobility.mobility_connector import mobility_connector
from task_geo.data_sources.mobility.mobility_formatter import mobility_formatter


def mobility():
    """Retrieve  the mobility reports from Google.

    Arguments:
        None

    Returns:
        pandas.DataFrame

    Example:
    >>> from task_geo.data_sources import get_data_source
    >>> mobility = get_data_source('mobility')
    >>> mobility()

    """
    raw = mobility_connector()
    return mobility_formatter(raw)
