from task_geo.data_sources.hdx.hdx_connector import hdx_acap_connector
from task_geo.data_sources.hdx.hdx_formatter import hdx_acap_formatter


def hdx_acap_api():
    """HDX Data Source

    Example:
    >>> hdx_acap_api()
    """
    raw = hdx_acap_connector()
    return hdx_acap_formatter(raw)
