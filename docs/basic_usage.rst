Basic Usage
-----------

The main contents of the task-geo are the data_sources it provides. The datasets should be uploaded to an storage
yet to be decided, for the other teams of coronawhy to use.

In case you needed access to a data source which still haven't been uploaded, there are many way to do so:

1. Using the example notebook for the data source in the notebooks folder.

2. Importing the data source and calling it yourself from a python script.

.. code-block:: python

    # First we import the helper functions
    >>> from task_geo.data_sources import list_data_sources, show_data_source_docs, get_data_source
    
    # We retrieve a list of available data sources.
    >>> list_data_sources()
    ['noaa_api']
    
    # We check the documentation of the data source,
    # so we see the specification of the arguments and the examples
    >>> show_data_source_docs('noaa_api')
    NOAA API Data Source.

        Arguments:
            countries(list[str]):
                List of country names in FIPS format.
            start_date(datetime):
                Start date for the data.
            end_date(datetime):
                End date for the date. (Optional, if not present will be set to the current day.)

        Example:
        >>> from datetime import datetime
        >>> countries = ['FR']
        >>> start_date = datetime(2020, 1, 1)
        >>> end_date = datetime(2020, 1, 15)
        >>> noaa_api(countries, start_date, end_date)

    # We retrieve the data source.
    >>> noaa_api = get_data_source('noaa_api')

    # At this point we can use the example or start hacking on our own.