from unittest import TestCase, skip

import pandas as pd

from task_geo.data_sources.noaa import noaa_api_formatter
from task_geo.testing import check_dataset_format


class TestNoaaApi(TestCase):

    def test_validate_formatter(self):
        """Validate formatter result according to Data Model."""
        # Setup
        raw = pd.read_csv('tests/fixtures/noaa_fixture.csv')

        # Run
        data = noaa_api_formatter(raw)

        # Check
        check_dataset_format(data)

    @skip
    def test_validate_formatter_country_avg(self):
        """Validate formatter result when country_avg is present."""
        # Setup
        raw = pd.read_csv('tests/fixtures/noaa_fixture.csv')

        # Run
        data = noaa_api_formatter(raw, country_avg=True)

        # Check
        check_dataset_format(data)
