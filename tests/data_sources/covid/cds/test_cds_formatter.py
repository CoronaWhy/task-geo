from unittest import TestCase

import pandas as pd

from task_geo.data_sources.covid.cds.cds_formatter import cds_formatter
from task_geo.testing import check_dataset_format


class TestCDSFormatter(TestCase):

    def test_cds_formatter(self):
        """Validate formatter output for datasource xxx."""
        # Setup
        fixture = pd.read_csv('tests/fixtures/cds.csv')

        # Run
        data = cds_formatter(fixture)

        # Check
        check_dataset_format(data)
