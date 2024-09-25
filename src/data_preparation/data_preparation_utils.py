"""
This module contains utils function for preparing the data for the EDA or model training
"""
# Import Standard Libraries
import os
import pandas as pd
import numpy as np
from pathlib import Path
from typing import List

# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def group_avg_column_by_frequency(data: pd.DataFrame,
                                  key: str,
                                  column: str,
                                  frequency: str,
                                  precision: int = 2) -> pd.DataFrame:
    """
    Group a DataFrame by the key with a frequency and compute the avg over the column

    Args:
        data: Pandas DataFrame to group by
        key: String key to group
        column: String column to compute the avg over
        frequency: String representing the frequency
        precision: Integer precision to round

    Returns:
        grouped_data: Pandas DataFrame with grouped data
    """

    logger.info('group_avg_column_by_frequency - Start')

    logger.info('group_avg_column_by_frequency - key: %s | frequency: %s | column: %s',
                key, frequency, column)

    # Define the grouper
    grouper = pd.Grouper(key=key, freq=frequency)

    # Group and compute average
    grouped_data = data.groupby(grouper)[column].mean().reset_index()

    # Round grouped data
    grouped_data[column] = grouped_data[column].round(precision)

    logger.info('group_avg_column_by_frequency - End')

    return grouped_data


def add_dummy_time_step(data: pd.DataFrame,
                        column_name: str = 'time_step') -> pd.DataFrame:
    """
    Add a dummy time-step feature called 'column_name' into the data

    Args:
        data: Pandas DataFrame to add the feature to
        column_name: String column name

    Returns:
        data: Pandas DataFrame with the added time-step column
    """

    logger.info('add_dummy_time_step - Start')

    logger.info('add_dummy_time_step - column_name: %s', column_name)

    # Compute the time-step
    time_step = np.arange(len(data))

    # Add the time-step to the data
    data[column_name] = time_step

    logger.info('add_dummy_time_step - End')

    return data


def add_lag_feature(data: pd.DataFrame,
                    column: str,
                    lag: int) -> pd.DataFrame:
    """
    Add a lag feature to the data

    Args:
        data: Pandas DataFrame to add lag to
        column: String column name to compute lag with
        lag: Integer lag value

    Returns:
        data: Pandas DataFrame with the lag feature added
    """
    logger.info('add_lag_feature - Start')

    logger.info('add_lag_feature - column: %s | lag: %s',
                column, lag)

    # Compute lag feature
    lag_feature = data.loc[:, column].shift(lag)

    # Add lag feature to the data
    data[column + '_lag_' + str(lag)] = lag_feature

    logger.info('add_lag_feature - End')

    return data


def add_seasonality(data: pd.DataFrame,
                    column: str,
                    seasonality: List[str]) -> pd.DataFrame:
    """
    Add all seasonality computed on the given 'column' into the 'data'

    Args:
        data: Pandas DataFrame to add seasonality to
        column: String column name to compute seasonality with
        seasonality: List of string seasonality to add
                     (values: day_of_week, week)

    Returns:
        data: Pandas DataFrame with the seasonality added
    """
    logger.info('add_seasonality - Start')

    # Fetch seasonality to add
    for element in seasonality:

        logger.info('add_seasonality - Seasonality: %s', element)

        # Switch between seasonality to add
        match element:
            case 'day_of_week':
                data['day_of_week'] = data[column].dt.day_name()
            case 'week':
                data['week'] = data[column].dt.isocalendar().week.astype('int32')
            case _:
                # Unrecognised seasonality
                raise ValueError('Unrecognised Seasonality')

    logger.info('add_seasonality - End')

    return data
