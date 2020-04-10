from unittest import TestCase

from task_geo.data_sources import list_data_sources
from task_geo.testing import check_data_source_package


class TestDataSourceModules(TestCase):
    """Check the module structure follows the guidelines.

    This is not a regular unittest, as it doesn't test the behavior of code,
    but rather checks that a data source is ready to be run and uploaded to cloud storage.
    """
    def test_data_sources(self):
        """Check data_source modules structure and outputs."""
        data_sources = list_data_sources()
        for data_source in data_sources:
            check_data_source_package(data_source, validate_output=False)
