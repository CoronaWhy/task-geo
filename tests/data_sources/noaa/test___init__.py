from datetime import datetime
from unittest import TestCase, skip

from task_geo.data_sources.noaa import noaa_api
from task_geo.testing import check_dataset_format


class TestNoaaApi(TestCase):

    @skip
    def test_validate_format_raw_output(self):
        """Validate datasource output.

        This tests is skipped intentionally on the main suite due to it taking to long.
        Is kept for developing porpouses.
        """
        # Setup
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2020, 1, 15)
        countries = ['BE']

        # Run
        data = noaa_api(countries, start_date, end_date)

        # Check
        check_dataset_format(data)
