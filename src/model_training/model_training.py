"""
The module contains classes for the Model Training pipelines and components
"""
# Import Standard Libraries
import pathlib
import pandas as pd
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

# Import Package Modules
from src.logging_module.logging_module import get_logger


class BoostedHybridModel:
    """
    The class implements a Boosted Hybrid Model for
    Time Series Forecasting, which learns trend and seasonal components
    through two distinct models.

    Attributes:
        linear_model: Linear model to extract trend component
        non_linear_model: Non-linear model to extract seasonality & cycle components
    """

    def __init__(self,
                 linear_model: LinearRegression,
                 non_linear_model: XGBRegressor):
        """
        Constructor for the BoostedHybridModel class

        Args:
            linear_model: Linear model to extract trend component
            non_linear_model: Non-linear model to extract seasonality & cycle components
        """
        # Setup logger
        self.logger = get_logger(__class__.__name__,
                                 pathlib.Path(__file__).parents[1] /
                                 'logging_module' /
                                 'log_configuration.yaml')

        self.logger.info('__init__ - Initialise object attributes')

        # Initialise object attributes
        self.linear_model = linear_model
        self.non_linear_model = non_linear_model

        # Initialise empty attributes
        self.linear_model_predictions = None
        self.residuals = None
        self.y_column_names = None

    def fit(self,
            trend_features: pd.DataFrame,
            serial_features: pd.DataFrame,
            y: pd.Series):
        """
        Fits the model to time series data

        Args:
            trend_features: Pandas dataframe containing trend features
            serial_features: Pandas dataframe containing serial features
            y: Pandas series containing target values

        Returns:
            Fitted models 'self.linear_model' and 'self.non_linear_model'
        """
        self.logger.info('fit - Start')

        self.logger.info('fit - Fit linear model')

        # Fit the linear model
        self.linear_model.fit(trend_features, y)

        self.logger.info('fit - Compute predictions')

        # Compute predictions of the Linear model to then calculate residuals
        self.linear_model_predictions = pd.DataFrame(
            self.linear_model.predict(trend_features),
            index=trend_features.index,
            columns=y.columns
        )

        self.logger.info('fit - Calculate residuals')

        # Calculate residuals
        self.residuals = y - self.linear_model_predictions

        # Stack residuals to fit a non-linear model
        self.residuals = self.residuals.stack().squeeze()

        self.logger.info('fit - Fit Non-linear model on serial features with residuals as target')

        # Fit the non-linear model on residuals
        self.non_linear_model.fit(serial_features, self.residuals)

        # Save column names
        self.y_column_names = y.columns

        self.logger.info('fit - End')
