"""
This test module includes all the tests for the
module src.model_training.model_training
"""
# Import Standard Modules
import pandas as pd
from statsmodels.tsa.deterministic import DeterministicProcess

# Import Package Modules
from src.model_training.model_training import BoostedHybridModel


# TODO: Fix the test function
def test_boosted_hybrid_model_fit(fixture_test_boosted_hybrid_model_data: pd.DataFrame,
                                  fixture_test_boosted_hybrid_model: BoostedHybridModel) -> bool:
    """
    Tests the src.model_training.model_training.BoostedHybridModel fit function

    Args:
        fixture_test_boosted_hybrid_model_data: Pandas dataframe containing test data
        fixture_test_boosted_hybrid_model: BoostedHybridModel object

    Returns:
    """
    # Define y
    y = fixture_test_boosted_hybrid_model_data.pop('Sales')

    # Define trend deterministic process for computing trend features
    trend_deterministic_process = DeterministicProcess(index=y.index,
                                                       constant=True,
                                                       order=2,
                                                       drop=True)

    # Define x for trend features
    x_trend = trend_deterministic_process.in_sample()

    # Define x for serial features
    x_serial = fixture_test_boosted_hybrid_model_data.stack()

    # Fit the model
    fixture_test_boosted_hybrid_model.fit(x_trend, x_serial, y)
