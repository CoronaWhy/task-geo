from unittest import TestCase

import pandas as pd

from task_geo.data_sources.mobility.mobility_formatter import mobility_formatter
from task_geo.testing import check_dataset_format


class TestMobilityFormatter(TestCase):

    def test_formatter_valid_output(self):
        """Check that the formatter output is compliant with the Data Model specification."""
        # Setup
        raw = pd.read_csv('tests/fixtures/mobility.csv')

        # Run
        data = mobility_formatter(raw)

        # Check
        check_dataset_format(data)
