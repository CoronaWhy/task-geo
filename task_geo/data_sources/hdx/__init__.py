from task_geo.data_sources.hdx.hdx_connector import hdx_acap_connector
from task_geo.data_sources.hdx.hdx_formatter import hdx_acap_formatter


def hdx_acap():
    """Retrieves formatted Government Measures Dataset from HDX DataSource
    Example:
    >>> hdx_acap()

    Returns: pandas.DataFrame
    """
    raw = hdx_acap_connector()
    return hdx_acap_formatter(raw)
