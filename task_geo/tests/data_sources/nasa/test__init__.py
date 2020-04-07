"""Test for NASA API."""

from unittest import TestCase

import pandas as pd
import numpy as np

from task_geo.data_sources.nasa import nasa
from task_geo.testing import check_dataset_format


class TestNasaAPI(TestCase):
    """Test for NASA API."""

    def test_validate_formatter(self):
        """Validate formatter result according to Data Model."""
        # Setup
        data = {
            'country': ['Japan'],
            'region': ['Hokkaido'],
            'sub_region': [np.nan],
            'lat': [43.066666],
            'lon': [141.350006]
        }
        data = pd.DataFrame(data)

        start_date = pd.to_datetime('01nov2019')

        df = nasa.nasa_meteo_data(data, start_date).iloc[:10]

        # Check.
        check_dataset_format(df)
