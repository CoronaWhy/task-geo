from task_geo.data_sources.hdx_acap.hdx_acap_connector import hdx_acap_connector
from task_geo.data_sources.hdx_acap.hdx_acap_formatter import hdx_acap_formatter


def hdx_acap():
    """Retrieves formatted Government Measures Dataset from HDX DataSource

    Arguments:
        None

    Returns:
        pandas.DataFrame

    Example:
    >>> from task_geo.data_sources import get_data_source
    >>> hdx_acap = get_data_source('hdx_acap')
    >>> data = hdx_acap()

    """
    raw = hdx_acap_connector()
    return hdx_acap_formatter(raw)
