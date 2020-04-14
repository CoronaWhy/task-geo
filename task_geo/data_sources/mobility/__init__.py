from task_geo.data_sources.mobility.mobility_connector import mobility_connector
from task_geo.data_sources.mobility.mobility_formatter import mobility_formatter


def mobility(download_folder, download):
    """ """
    raw = mobility_connector(download_folder, download)
    return mobility_formatter(raw)
