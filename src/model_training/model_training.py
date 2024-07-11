"""
The module contains object classes for the Model Training pipelines and components
"""
# Import Standard Libraries
import pathlib
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

# Import Package Modules
from src.logging_module.logging_module import get_logger


class BoostedHybridModel:
    """
    The class implements a Boosted Hybrid Model for
    Time Series Forecasting.

    Attributes:
        linear_model: Linear model to extract trend component
        non_linear_model: Non-linear model to extract seasonality & cycle components
    """

    def __init__(self,
                 linear_model: LinearRegression,
                 non_linear_model: XGBRegressor):
        pass

    def fit(self, X, y):
        pass
