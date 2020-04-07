"""Example utilization of the NASA data sourcing."""

import numpy as np
import pandas as pd
from nasa import nasa_meteo_data


def main():
    """
    Parse an example dataset of meteo data for Hokkaido, Japan to csv.

    Returns
    -------
    None.

    """
    data = {
        'country': ['Japan'],
        'region': ['Hokkaido'],
        'sub_region': [np.nan],
        'lat': [43.066666],
        'lon':	[141.350006]
        }
    data = pd.DataFrame(data)

    start_date = pd.to_datetime('01nov2019')

    df = nasa_meteo_data(data, start_date).iloc[:10]

    df.to_csv("nasa_example.csv", index=False)


if __name__ == "__main__":
    main()
