from unittest import TestCase

import pandas as pd

from task_geo.testing import (
    check_column_and_get_index, check_dataset_format, get_geographical_granularity)


class TestGetGeographicalGranularity(TestCase):

    def test_simple_case(self):
        """If a term is present, the index is returned."""
        # Setup
        data = pd.DataFrame(columns=['city'])

        expected_result = 0

        # Run
        result = get_geographical_granularity(data)

        # Check
        assert result == expected_result

    def test_unordenerd_names(self):
        """If the column has all the terms, it returns the lowest granularity."""
        # Setup
        data = pd.DataFrame(columns=['country', 'region', 'subregion', 'city'])

        expected_result = 0

        # Run
        result = get_geographical_granularity(data)

        # Check
        assert result == expected_result


class TestCheckColumnAndGetIndex(TestCase):

    def test_valid_case(self):
        """If the column is present, the index is returned."""
        # Setup
        data = pd.DataFrame(columns=['test'])
        name = 'test'
        reference = 'required'

        expected_result = 0
        # Run
        result = check_column_and_get_index(name, data, reference)

        # Check
        assert result == expected_result

    def test_exception_raised(self):
        """If the column is not present, an AssertionError is raised."""
        # Setup
        data = pd.DataFrame(columns=[''])
        name = 'required'
        reference = 'value'
        expected_exception_message = 'If value is provided, required should be present too'

        # Run
        with(self.assertRaises(AssertionError)) as error:
            check_column_and_get_index(name, data, reference)

        # Check
        assert error.exception.args[0] == expected_exception_message


class TestCheckDatasetFormat(TestCase):

    def test_lowercase_columns(self):
        """If all columns are lowercase no error is raised"""
        # Setup
        data = pd.DataFrame([{
            'a': 0.0,
            'country': 'xxx'
        }])

        # Run / Check
        check_dataset_format(data)

    def test_ordered_geopolitical_divisions(self):
        """If all 4 levels of geopolitical divisions are present and ordered, this test passes."""
        # Setup
        data = pd.DataFrame([{
            'country': 'xxx',
            'region': 'yyy',
            'sub_region': 'zzzz',
            'city': 'ttt'
        }])

        # Run / Check
        check_dataset_format(data)

    def test_unordered_geopolitical_divisions(self):
        # Setup
        data = pd.DataFrame([{
            'city': 'ttt',
            'country': 'xxx',
            'region': 'yyy',
            'sub_region': 'zzzz',
        }])

        expected_exception_message = (
            'The correct ordening of the columns is "country, region, sub_region, city"'
        )

        # Run
        with self.assertRaises(AssertionError) as error:
            check_dataset_format(data)

        # Check
        assert error.exception.args[0] == expected_exception_message

    def test_missing_ordered_geopolitical_divisions(self):
        """If lower geopolitical levels are missing, but well ordered, no exeption is raised."""
        # Setup
        data = pd.DataFrame([{
            'country': 'xxx',
            'region': 'yyy',
        }])

        # Run / Check
        check_dataset_format(data)

    def test_missing_unordered_geopolitical_divisions(self):
        """If lower geopolitical levels are missing, and unordered, and exception is raised."""
        # Setup
        data = pd.DataFrame([{
            'region': 'yyy',
            'country': 'xxx',

        }])

        expected_exception_message = (
            'The correct ordening of the columns is "country, region, sub_region, city"'
        )

        # Run
        with self.assertRaises(AssertionError) as error:
            check_dataset_format(data)

        # Check
        assert error.exception.args[0] == expected_exception_message
