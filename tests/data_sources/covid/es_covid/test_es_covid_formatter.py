from unittest import TestCase

import pandas as pd

from task_geo.data_sources.covid.es_covid import es_covid_formatter
from task_geo.testing import check_dataset_format


class TestEsCovid(TestCase):

    def test_validate_formatter(self):
        """ Validate formatter result according to Data Model"""
        # Setup
        raw = pd.read_csv('tests/fixtures/es_covid_fixture.csv')

        # Run
        data = es_covid_formatter(raw)

        # Check.
        check_dataset_format(data)
