from task_geo.data_sources.noaa.noaa_api_connector import noaa_api_connector
from task_geo.data_sources.noaa.noaa_api_formatter import noaa_api_formatter


def noaa_api(countries, start_date, end_date=None, metrics=None, country_aggr=False):
    """NOAA API Data Source.

    Please, note the following:
        - The metrics variable will only filter out available metrics, if the metric is not
          available, requesting it will have no effect.

        - Country_agg will only return the min for `TMIN`, that is the absolute minimum,
          and the max for `TMAX`, the absolute maximum.


    Arguments:
        countries(list[str]):
            List of country names in FIPS format.
        start_date(datetime):
            Start date for the data.
        end_date(datetime):
            End date for the date. (Optional, if not present will be set to the current day.)
        metrics(list[str]): Optional.List of metrics to retrieve,valid values are:
            TMIN: Minimum temperature.
            TMAX: Maximum temperature.
            TAVG: Average of temperature.
            SNOW: Snowfall (mm).
            SNWD: Snow depth (mm).
            PRCP: Precipitation.

        country_aggr(bool): When True, only an aggregate for each date/country will be returned.

    Example:
    >>> from datetime import datetime
    >>> countries = ['FR']
    >>> start_date = datetime(2020, 1, 1)
    >>> end_date = datetime(2020, 1, 15)
    >>> noaa_api(countries, start_date, end_date)
    """
    raw = noaa_api_connector(countries, start_date, end_date, metrics)
    return noaa_api_formatter(raw, metrics, country_aggr)
