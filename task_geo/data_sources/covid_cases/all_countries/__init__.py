from task_geo.data_sources.covid_cases.all_countries import cds_connector
from task_geo.data_sources.covid_cases.all_countries import cds_formatter


def cds_api(country):
    raw = cds_connector(country)
    return cds_formatter(raw)
