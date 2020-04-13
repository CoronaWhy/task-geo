from task_geo.data_sources.covid.nyt.nyt_connector import nyt_connector
from task_geo.data_sources.covid.nyt.nyt_formatter import nyt_formatter


def nyt():
    """Data source for US COVID-19 cases (per county), coming from The New York Times.

    Arguments:
        None

    Returns:
        pandas.DataFrame
    """
    data = nyt_connector()
    return nyt_formatter(data)
