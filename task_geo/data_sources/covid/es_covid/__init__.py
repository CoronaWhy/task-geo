from task_geo.data_sources.covid.es_covid.es_covid_connector import es_covid_connector
from task_geo.data_sources.covid.es_covid.es_covid_formatter import es_covid_formatter


def es_covid():
    """Daily updates for cases for Spain, joined with static demographic data.

    The following sources are updated on each run:
    1. https://covid19.isciii.es/ provides the following

        - autonomous_community_iso
        - date
        - cases
        - hospitalized
        - intensive care unit (icu)
        - deceased
        - recovered

    The following sources were used for one time access:
    1. https://en.wikipedia.org/wiki/Autonomous_communities_of_Spain provides the
    following 19 Spanish Autonomous Communities

        - area
        - population
        - density
        - gdp_per_capita_euros

    Arguments:
        None

    Returns:
        pandas.DataFrame

    """
    data = es_covid_connector()
    return es_covid_formatter(data)
