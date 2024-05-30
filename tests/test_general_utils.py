"""
This test module includes all the tests for the
module src.general.general_utils
"""
# Import Standard Modules
import pathlib
import pytest

# Import Package Modules
from src.general_utils.general_utils import (
    read_configuration,
    build_path_from_list
)


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    (pathlib.Path(__file__).parents[1]
     / 'configuration'
     / 'test_config.yaml',
     'test_value',
     1),
])
def test_read_configuration(test_config_file: pathlib.Path,
                            test_config: str,
                            expected_value: int) -> bool:
    """
    Test the function src.general_utils.general_utils.read_configuration
    by reading test configuration entries

    Args:
        pathlib.Path: Configuration file path
        test_config: String configuration entry key
        expected_value: String configuration expected value

    Returns:
    """

    # Read configuration file
    config = read_configuration(test_config_file)

    assert config[test_config] == expected_value


@pytest.mark.parametrize('test_config_file, expected_error', [
    (pathlib.Path(__file__).parents[1]
     / 'configuration'
     / 'wrong_config.yaml',
     FileNotFoundError)
])
def test_read_configuration_exceptions(test_config_file: pathlib.Path,
                                       expected_error: FileNotFoundError) -> bool:
    """
    Test the exceptions to the function
    src.general_utils.general_utils.read_configuration

    Args:
        test_config_file: Wrong configuration file path
        expected_error: Exception instance

    Returns:
    """

    with pytest.raises(expected_error):
        read_configuration(test_config_file)


@pytest.mark.parametrize('path_list, expected_absolute_path', [
    (
            [
                'data',
                'raw',
                'test_data.csv'
            ],
            pathlib.Path(__file__).parents[1] /
            'data' /
            'raw' /
            'test_data.csv'
    )
])
def test_build_path_from_list(path_list: list,
                              expected_absolute_path: pathlib.Path) -> bool:
    """
    Test the function src.general_utils.general_utils.build_path_from_list
    by comparing built absolute path with the expected ome

    Args:
        path_list: list of relative path sub-folders
        expected_absolute_path: pathlib.Path expected built absolute path

    Returns:
    """

    # Build the absolute path
    absolute_path = build_path_from_list(path_list)

    assert absolute_path.resolve() == expected_absolute_path.resolve()
