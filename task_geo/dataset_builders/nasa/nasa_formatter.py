"""Extract meteorological data from NASA.

Source:
https://power.larc.nasa.gov/
"""
import itertools
import pandas as pd
from nasa import PARAMETERS, COL_NAMES


def nasa_formatter(df_nasa, parms):
    """
    Format the NASA data.

    Parameters
    ----------
    df_nasa : pandas.DataFrame
    parms : list of strings

    Returns
    -------
    df_nasa : pandas.DataFrame

    """
    # date column
    df_nasa.reset_index(inplace=True, drop=False)
    df_nasa.rename(columns={'index': 'date'}, inplace=True)
    df_nasa['date'] = pd.to_datetime(df_nasa['date'], format='%Y%m%d')

    # reorder columns
    base_parms = ['lon', 'lat', 'date']
    all_parms = list(itertools.chain.from_iterable([PARAMETERS[p]
                                                    for p in parms]))
    df_nasa = df_nasa[base_parms + all_parms]

    # rename columns
    df_nasa.rename(columns=COL_NAMES, inplace=True)

    return df_nasa
