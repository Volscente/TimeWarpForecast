"""
This test module includes all the tests for the
module src.model_training.model_training
"""
# Import Standard Modules
import pandas as pd
import pathlib
import pytest

# Import Package Modules
from src.model_training.model_training import BoostedHybridModel


def test_boosted_hybrid_model_fit(fixture_test_boosted_hybrid_model_data: pd.DataFrame,
                                  fixture_test_boosted_hybrid_model: BoostedHybridModel) -> bool:
    """
    Tests the src.model_training.model_training.BoostedHybridModel fit function

    Args:
        fixture_test_boosted_hybrid_model_data: Pandas dataframe containing test data
        fixture_test_boosted_hybrid_model: BoostedHybridModel object

    Returns:
    """
    # Fit the model
    fixture_test_boosted_hybrid_model.fit(fixture_test_boosted_hybrid_model_data)
