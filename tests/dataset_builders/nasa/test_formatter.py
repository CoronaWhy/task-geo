"""Test for NASA API."""

from unittest import TestCase

import pandas as pd

from task_geo.dataset_builders.nasa.nasa_formatter import nasa_formatter
from task_geo.testing import check_dataset_format


class TestNasaAPI(TestCase):
    """Test for NASA API."""

    def test_validate_formatter(self):
        """Validate formatter result according to Data Model."""
        # Setup
        raw = pd.read_csv('tests/fixtures/nasa.csv', index_col=0)

        data = nasa_formatter(raw)

        # Check.
        check_dataset_format(data)
