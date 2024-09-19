"""
This test module includes all the tests for the
module src.data_preparation
"""
# Import Standard Modules
import pandas as pd
import pathlib
import pytest

# Import Package Modules
from src.data_preparation.data_preparation_utils import (
    group_avg_column_by_frequency,
    add_dummy_time_step,
    add_lag_feature
)


@pytest.mark.parametrize('dataset_name, key, column, frequency, index, expected_output', [
    ('fixture_data_preparation_dataset', 'date', 'transactions', 'W', 1, 1641.09)
])
def test_group_avg_column_by_frequency(dataset_name: str,
                                       key: str,
                                       column: str,
                                       frequency: str,
                                       index: int,
                                       expected_output: float,
                                       request: pytest.FixtureRequest) -> bool:
    """
    Test the function src.data_preparation.data_preparation_utils.group_avg_column_by_frequency

    Args:
        dataset_name: String name of the dataset
        key: String key to group
        column: String column to compute the avg over
        frequency: String representing the frequency
        index: Integer index of the row to test
        expected_output: float expected grouped value for the column
        request: pytest.FixtureRequest required to get the dataset fixtures

    Returns:
    """
    # Retrieve dataset fixture
    dataset = request.getfixturevalue(dataset_name)

    # Apply the function to test
    grouped_data = group_avg_column_by_frequency(data=dataset, key=key, column=column, frequency=frequency)

    assert grouped_data.loc[index, column] == expected_output


@pytest.mark.parametrize('dataset_name, column, expected_output', [
    ('fixture_data_preparation_dataset', 'time_step', 3)
])
def test_add_dummy_time_step(dataset_name: str,
                             column: str,
                             expected_output: int,
                             request: pytest.FixtureRequest) -> bool:
    """
    Test the function src.data_preparation.data_preparation_utils.add_dummy_time_step

    Args:
        dataset_name: String name of the dataset
        column: String column name of time-step feature
        expected_output: Integer expected time-step feature value
        request: pytest.FixtureRequest required to get the dataset fixtures

    Returns:
    """
    # Retrieve dataset fixture
    dataset = request.getfixturevalue(dataset_name)

    # Apply function to test
    dataset = add_dummy_time_step(data=dataset)

    assert dataset.loc[expected_output, column] == expected_output


@pytest.mark.parametrize('dataset_name, column, lag, index, expected_output', [
    ('fixture_data_preparation_dataset', 'transactions', 2, 3, 2111.0)
])
def test_add_lag_feature(dataset_name: str,
                         column: str,
                         lag: int,
                         index: int,
                         expected_output: float,
                         request: pytest.FixtureRequest) -> bool:
    """
    Test the function src.data_preparation.data_preparation_utils.add_lag_feature

    Args:
        dataset_name: String name of the dataset
        column: String column name of lag feature
        lag: Integer lag value
        index: Integer index of the row to test
        expected_output: Float expected lag feature value
        request: pytest.FixtureRequest required to get the dataset fixtures

    Returns:
    """
    # Retrieve dataset fixture
    dataset = request.getfixturevalue(dataset_name)

    # Apply function to test
    dataset = add_lag_feature(data=dataset, column=column, lag=lag)

    assert dataset.loc[index, column + '_lag_' + str(lag)] == expected_output
