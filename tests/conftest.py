"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pytest

# Import Package Modules
from src.general_utils.general_utils import read_configuration

# Read configuration file
configuration = read_configuration(pathlib.Path(__file__).parents[1]
                                   / 'configuration'
                                   / 'test_config.yaml')


@pytest.fixture
def fixture_data_config(test_data_config: dict = configuration['test_data_config']):
    """
    Fixture for a Dictionary test data config with structure:
        <data_config_name>:
            data_path: list[str]
            date_columns: list[str]
            delimiter: str

    Args:
        test_data_config: Dictionary of data configuration

    Returns:
        test_data_config: Dictionary of data configuration
    """

    return test_data_config


@pytest.fixture
def fixture_exception_data_config(test_exception_data_config: dict = configuration['test_exception_data_config']):
    """
    Fixture for a Dictionary test exception data config with structure:
        <data_config_name>:
            data_path: list[str]
            date_columns: list[str]
            delimiter: str

    Args:
        test_exception_data_config: Dictionary of data configuration

    Returns:
        exception_test_data_config: Dictionary of data configuration
    """

    return test_exception_data_config