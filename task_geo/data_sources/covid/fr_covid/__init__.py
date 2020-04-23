"""Retrieve granular data of COVID-19 cases in France.

Functions:
    - fr_covidata_connector: Extracts data from CSV URL
    - fr_covidata_formatter: Cleans CSV data
    - fr_covidata: Combines the two previous functions

Data Credits:
    OpenCOVID19-fr
    https://www.data.gouv.fr/en/datasets/chiffres-cles-concernant-lepidemie-de-covid19-en-france/
    https://github.com/opencovid19-fr/data

"""


from task_geo.data_sources.covid.fr_covid.fr_covid_connector import fr_covid_connector
from task_geo.data_sources.covid.fr_covid.fr_covid_formatter import fr_covid_formatter


def fr_covidata():
    """Retrieve and format granular data of COVID-19 cases in France.

    Arguments:
        None

    Returns:
        pandas.DataFrame

    """
    df = fr_covid_connector()
    return fr_covid_formatter(df)
