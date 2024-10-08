"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

# Import Package Modules
from src.general_utils.general_utils import (
    read_configuration,
    read_data_from_config
)
from src.model_training.model_training import BoostedHybridModel

# Read configuration file
configuration = read_configuration(pathlib.Path(__file__).parents[1]
                                   / 'configuration'
                                   / 'test_config.yaml')


@pytest.fixture
def fixture_data_config(test_data_config: dict = configuration['test_data_config']) -> dict:
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
def fixture_exception_data_config(
        test_exception_data_config: dict = configuration['test_exception_data_config']
) -> dict:
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


@pytest.fixture
def fixture_test_boosted_hybrid_model_data(
        data_config: dict = configuration['test_boosted_hybrid_model_data_config']
) -> bool:
    """
    Fixture for Pandas DataFrame test data for a Boosted Hybrid Model

    Args:
        data_config: Dictionary of data configuration

    Returns:
        data: Pandas DataFrame test data for a Boosted Hybrid Model
    """
    # Read data
    data = read_data_from_config(data_config)

    # Set Index
    data.index = data['Month']

    # Convert index to 'Day' period and reindex with only required columns
    data = data.to_period('D').reindex(columns=['BuildingMaterials',
                                                'FoodAndBeverage'])

    # Refine dataframe structure
    data = pd.concat({'Sales': data}, names=[None, 'Industries'], axis=1)

    return data


@pytest.fixture
def fixture_test_boosted_hybrid_model() -> BoostedHybridModel:
    """
    Fixture for an object of class src.model_training.model_training.BoostedHybridModel

    Returns:
        model: BoostedHybridModel object instance
    """
    # Instance the object
    model = BoostedHybridModel(LinearRegression(),
                               XGBRegressor())

    return model


@pytest.fixture
def fixture_data_preparation_dataset(
        data_config: dict = configuration['test_data_preparation_dataset']
) -> pd.DataFrame:
    """
    Fixture for a Pandas DataFrame of data preparation dataset

    Args:
        data_config: Dictionary of data configuration

    Returns:
        data: Pandas DataFrame of data preparation dataset
    """
    # Read data
    data = read_data_from_config(data_config)

    return data
