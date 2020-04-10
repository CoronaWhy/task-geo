from unittest import TestCase
from unittest.mock import patch

from task_geo.data_sources import execute_data_source, get_default_parameters


class TestGetDefaultParameters(TestCase):

    @patch.dict(
        'task_geo.data_sources.DATA_SOURCE_DEFAULT_PARAMETERS',
        {'data_source_name': {'args': 'xxx', 'kwargs': 'yyy'}}
    )
    def test_simple_case(self):
        """get_default_parameters returns `args` and `kwargs` keys of default parameters dict."""
        # Setup
        name = 'data_source_name'

        expected_result = ('xxx', 'yyy')
        # Run
        result = get_default_parameters(name)

        # Check
        assert expected_result == result


class TestExecuteDataSource(TestCase):

    @patch('task_geo.data_sources.get_data_source')
    @patch('task_geo.data_sources.get_default_parameters')
    def test_simple_case(self, parameters_mock, get_data_source_mock):
        """execute_data_source retrieves the data_source, arguments, and make the call."""
        # Setup
        name = 'data_source_name'

        data_source = get_data_source_mock.return_value
        data_source.return_value = 'data from the data source'

        parameters_mock.return_value = (['xxx'], {'yyy': 'zzz'})

        expected_result = 'data from the data source'

        # Run
        result = execute_data_source(name)

        # Check
        assert result == expected_result

        get_data_source_mock.assert_called_once_with('data_source_name')
        data_source.assert_called_once_with('xxx', yyy='zzz')
        parameters_mock.assert_called_once_with('data_source_name')
