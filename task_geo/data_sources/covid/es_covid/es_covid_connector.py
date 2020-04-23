import pandas as pd


def es_covid_connector():
    """Retrieve data from https://covid19.isciii.es.

    Arguments:
        None

    Returns:
        pandas.DataFrame

    """
    url = "https://covid19.isciii.es/resources/serie_historica_acumulados.csv"
    return pd.read_csv(url, encoding="latin_1")
