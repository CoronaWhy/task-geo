import os
from unittest import TestCase, skipUnless

from task_geo.data_sources import list_data_sources
from task_geo.testing import check_data_source_package


@skipUnless(os.environ.get('test_module_structure'), 'Missing test_module_structure')
class TestDataSourceModules(TestCase):
    """Check the module structure follows the guidelines.

    This is not a regular unittest, as it doesn't test the behavior of code,
    but rather checks that a data source is ready to be run and uploaded to cloud storage.

    The behavior of this test can be changed using environment variables to better integrate it
    with CI systems:

    - test_module_structure: This variable determines wheter or not skip this class
    - test_data_source_output: This variable determines wheter or not check the output of the
        datasource.

    """
    def test_data_sources(self):
        """Check data_source modules structure and outputs."""
        data_sources = list_data_sources()
        validate_output = os.environ.get('test_data_source_output')
        for data_source in data_sources:
            check_data_source_package(data_source, validate_output=validate_output)
