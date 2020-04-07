from task_geo.data_sources.covid.spain.es_covid_connector import es_covid_connector
from task_geo.data_sources.covid.spain.es_covid_formatter import es_covid_formatter

"""
This module provides importing daily updates for cases, mixed with static demographic data.

Overview:

    Discovery
        Dynamic
            The following sources are updated on each run:
                1. https://covid19.isciii.es/ provides the following
                 - autonomous_community_iso
                 - date
                 - cases
                 - hospitalized
                 - intensive care unit (icu)
                 - deceased
                 - recovered

        Static
            The following sources were used for one time access:
             1. https://en.wikipedia.org/wiki/Autonomous_communities_of_Spain provides the
                following 19 Spanish Autonomous Communities
              - area
              - population
              - density
              - gdp_per_capita_euros
    """


def es_covid():
    """
    Data Source for Spain

    Arguments:
        N/A

    Returns:
        pandas.DataFrame
    """
    data = es_covid_connector()
    return es_covid_formatter(data)
