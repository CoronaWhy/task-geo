from task_geo.data_sources.hdx.hdx_connector import acap_connector
from task_geo.data_sources.hdx.hdx_formatter import acap_formatter


def hdx_api():
    """HDX Data Source

    Example:
    >>> hdx_api()
    """
    raw = acap_connector()
    return acap_formatter(raw)
