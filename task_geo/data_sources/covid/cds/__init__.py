from task_geo.data_sources.covid.cds.cds_connector import cds_connector
from task_geo.data_sources.covid.cds.cds_formatter import cds_formatter


def cds(country=None):
    """CoronaDataScraper Data Source.

    This data source has two ways of working:
    - When given the country it will return a pandas.DataFrame with the data for the given country.
    - When no argument is given, returns the raw data.

    Arguments:
        country[str]: 3 letter ISO country code.Optional

    Returns:
        pandas.DataFrame
    """
    data = cds_connector(country)

    return cds_formatter(data)
