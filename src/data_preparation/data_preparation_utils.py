"""
This module contains utils function for preparing the data for the EDA or model training
"""
# Import Standard Libraries
import os
import pandas as pd
from pathlib import Path

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
                                  frequency: str) -> pd.DataFrame:
    """
    Group a DataFrame by the key with a frequency and compute the avg over the column

    Args:
        data: Pandas DataFrame to group by
        key: String key to group
        column: String column to compute the avg over
        frequency: String representing the frequency

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

    logger.info('group_avg_column_by_frequency - End')

    return grouped_data
