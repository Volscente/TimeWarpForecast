"""
The module contains several util functions for performing exploratory data analysis.
"""
# Import Standard Libraries
import os
from pathlib import Path
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import seaborn as sns

# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def set_plot_characteristics(plot_characteristics: dict) -> None:
    """
    Sets up the Seaborn theme with the specified plot_characteristics.

    Args:
        plot_characteristics: Dictionary of Seaborn theme parameters, style and palette.

    Returns:
    """
    logger.info('set_plot_characteristics - Start')

    logger.info('set_plot_characteristics - Creating theme parameters')

    # Define theme parameters
    theme_parameters = {
        'axes.spines.right': plot_characteristics['theme_parameters']['axes_spines_right'],
        'axes.spines.top': plot_characteristics['theme_parameters']['axes_spines_top'],
        'grid.alpha': plot_characteristics['theme_parameters']['grid_alpha'],
        'figure.figsize': (plot_characteristics['theme_parameters']['figure_figsize'][0],
                           plot_characteristics['theme_parameters']['figure_figsize'][1]),
        'font.family': plot_characteristics['theme_parameters']['font_family'],
        'axes.titlesize': plot_characteristics['theme_parameters']['axes_titlesize'],
        'figure.facecolor': plot_characteristics['theme_parameters']['figure_facecolor'],
        'axes.facecolor': plot_characteristics['theme_parameters']['axes_facecolor']
    }

    # Set the theme
    sns.set_theme(style=plot_characteristics['style'],
                  palette=sns.color_palette(plot_characteristics['color_palette']),
                  rc=theme_parameters)

    logger.info('set_plot_characteristics - End')


def plot_time_series(time_series: pd.DataFrame,
                     columns: Tuple[str, str],
                     title: str,
                     labels: Tuple[str, str, str],
                     to_plot: bool) -> matplotlib.axes.Axes:
    """
    Plots a time series using seaborn matplotlib Axes.

    Args:
        time_series: Pandas dataframe with time series
        columns: Tuple of String name of columns in time_series for x-axis nad y-axis
        title: String title of plot
        labels: Tuple of three strings containing labels for x-axis and y-axis and for the plot
        to_plot: Boolean indicating whether to plot the time series or return the axes

    Returns:
        ax: matplotlib Axes with time series plot
    """
    logger.info('plot_time_series - Start')

    logger.info('plot_time_series - Plot time series')

    # Plot the data
    ax = sns.lineplot(data=time_series,
                      x=time_series[columns[0]],
                      y=time_series[columns[1]],
                      label=labels[2])

    logger.info('plot_time_series - Set plot configurations')

    # Set title
    ax.set_title(title,
                 fontweight='bold',
                 fontsize=20)

    # Set tick rotation
    ax.tick_params(labelrotation=45)

    # Set Labels
    ax.set_xlabel(labels[0],
                  fontsize=14)
    ax.set_ylabel(labels[1],
                  fontsize=14)

    # Set the legend
    ax.legend(loc='upper center',
              bbox_to_anchor=(0.5, 0.95),
              fontsize=12,
              ncol=2)

    # Switch for plotting or returning the axes
    if to_plot:
        logger.info('plot_time_series - Calling the plt.show()')

        # Show plt
        plt.show()

        # Define the layout
        plt.tight_layout()

    logger.info('plot_time_series - End')

    return ax


def plot_predictions_vs_time_series(data: Tuple[pd.DataFrame, np.ndarray],
                                    columns: Tuple[str, str],
                                    title: str,
                                    labels: Tuple[str, str, str],
                                    to_plot: bool) -> matplotlib.axes.Axes:
    """
    Plot the predicted values against the time series

    Args:
        data: Tuple of Pandas DataFrame with time series and Numpy array with predicted values
        columns: Tuple of String name of columns in time_series for x-axis nad y-axis
        title: String title of plot
        labels: Tuple of three strings containing labels for x-axis and y-axis and for the plot
        to_plot: Boolean indicating whether to plot the time series or return the axes

    Returns:
        ax_predictions: matplotlib Axes with predicted values against the time series plot
    """
    logger.info('plot_predictions_vs_time_series - Start')

    logger.info('plot_predictions_vs_time_series - Extract time series and predictions')

    # Extract time series and predictions from data
    time_series, predictions = data[0], data[1]

    logger.info('plot_predictions_vs_time_series - Plot tim series')

    # Plot time series
    ax_time_series = plot_time_series(time_series=time_series,
                                      columns=columns,
                                      title=title,
                                      labels=(labels[0], labels[1], 'Time Series'),
                                      to_plot=False)

    logger.info('plot_predictions_vs_time_series - Plot predicted values')

    # Plot predictions
    ax_predictions = sns.lineplot(x=time_series[columns[0]],
                                  y=predictions,
                                  label=labels[2],
                                  ax=ax_time_series)

    # Define legend settings
    ax_predictions.legend(loc='upper center',
                          bbox_to_anchor=(0.5, 1.03),
                          fontsize=12,
                          ncol=2)

    # Switch for plotting or returning the axes
    if to_plot:
        logger.info('plot_predictions_vs_time_series - Calling the plt.show()')

        # Show plt
        plt.show()

        # Define the layout
        plt.tight_layout()

    logger.info('plot_predictions_vs_time_series - End')

    return ax_predictions


def plot_moving_average(time_series: pd.DataFrame,
                        rolling_settings: dict,
                        columns: Tuple[str, str],
                        title: str,
                        labels: Tuple[str, str, str]) -> matplotlib.axes.Axes:
    """

    Args:
        time_series:
        rolling_settings:
        columns:
        title:
        labels:

    Returns:

    """
    logger.info('plot_moving_average - Start')

    logger.info('plot_moving_average - Setting index')

    # Set index
    time_series_indexed = time_series.set_index(columns[0])

    logger.info('plot_moving_average - Computing the moving average')

    # Compute moving average
    moving_average = time_series_indexed.rolling(
        window=rolling_settings['window'],
        center=rolling_settings['center'],
        min_periods=rolling_settings['min_periods']
    ).mean()

    # Extract only relevant column
    moving_average = moving_average[columns[1]]

    logger.info('plot_moving_average - Plot time series')

    # Plot time series
    ax_time_series = plot_time_series(time_series=time_series,
                                      columns=columns,
                                      title=title,
                                      labels=(labels[0], labels[1], 'Time Series'),
                                      to_plot=False)

    logger.info('plot_moving_average - Plot moving average')

    # Plot moving average
    ax_moving_average = sns.lineplot(x=time_series[columns[0]],
                                     y=moving_average,
                                     label=labels[2],
                                     ax=ax_time_series)

    logger.info('plot_moving_average - Set plot configurations')

    # Define legend settings
    ax_moving_average.legend(loc='upper center',
                             bbox_to_anchor=(0.5, 1.03),
                             fontsize=12,
                             ncol=2)

    # Show plt
    plt.show()

    # Define the layout
    plt.tight_layout()

    logger.info('plot_moving_average - End')

    return ax_moving_average
