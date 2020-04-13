"""us_census data source.

Data Credits:
    The United States Census Bureau
    https://data.census.gov/
"""
from task_geo.data_sources.demographics.us_census.us_census_connector import us_census_connector
from task_geo.data_sources.demographics.us_census.us_census_formatter import us_census_formatter


def us_census():
    """Data Source for the US census.

    Arguments:
        None

    Returns:
        pandas.DataFrame
    """
    df = us_census_connector()
    return us_census_formatter(df)
