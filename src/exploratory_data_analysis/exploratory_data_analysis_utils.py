"""
The module contains several util functions for performing exploratory data analysis.
"""
# Import Standard Libraries
import os
import math
from pathlib import Path
from typing import Tuple
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import pandas as pd
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


def plot_regression_plot(data: pd.DataFrame,
                         columns: Tuple[str, str],
                         title: str,
                         labels: Tuple[str, str],
                         to_plot: bool) -> matplotlib.axes.Axes:
    logger.info('plot_regression_plot - Start')

    logger.info('plot_regression_plot - Plot time series')

    # Plot time series
    ax_time_series = plot_time_series(time_series=data,
                                      columns=columns,
                                      title=title,
                                      labels=(labels[0], labels[1], 'Time Series'),
                                      to_plot=False)

    logger.info('plot_regression_plot - Plot regression plot')

    # Plot regression plot
    ax_regression_plot = sns.regplot(data=data,
                                     x=columns[0],
                                     y=columns[1],
                                     scatter_kws=dict(color='0.75'),
                                     label='Predictions',
                                     ax=ax_time_series)

    # Define legend settings
    ax_regression_plot.legend(loc='upper center',
                              bbox_to_anchor=(0.5, 1.03),
                              fontsize=12,
                              ncol=3)

    # Switch for plotting or returning the axes
    if to_plot:
        logger.info('plot_regression_plot - Calling the plt.show()')

        # Show plt
        plt.show()

        # Define the layout
        plt.tight_layout()

    logger.info('plot_regression_plot - End')

    return ax_regression_plot


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

    logger.info('plot_predictions_vs_time_series - Plot time series')

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


def plot_single_lag(data: pd.Series,
                    lag_value: int,
                    ax: matplotlib.axes.Axes) -> matplotlib.axes.Axes:
    """
    Plot a time series against a specific lag with its correlation value

    Args:
        data: Pandas series with time series
        lag_value: Integer indicating lag to plot
        ax: Matplotlib Axes object

    Returns:
        ax: Matplotlib Axes object with lag plot
    """
    logger.info('plot_single_lag - Start')

    # Create the lag data by shifting the time steps
    lag_data = data.shift(lag_value)

    # Compute correlation value
    corr = data.corr(lag_data)

    # Scatter plot settings
    scatter_kws = {
        'alpha': 0.75,
        's': 3
    }

    # Line plot settings
    line_kws = {'color': 'C3'}

    logger.info('plot_single_lag - Plotting lag %s', lag_value)

    # Plot the data
    ax = sns.regplot(x=lag_data,
                     y=data,
                     scatter_kws=scatter_kws,
                     line_kws=line_kws,
                     lowess=True,
                     ax=ax)

    # Plot the correlation
    at = AnchoredText(
        f"{corr:.2f}",
        prop={'size': 'large'},
        frameon=True,
        loc="upper left",
    )

    # Refine the plot settings
    at.patch.set_boxstyle("square, pad=0.0")
    ax.add_artist(at)
    ax.set(title=f"Lag {lag_value}")

    logger.info('plot_single_lag - End')

    return ax


def plot_moving_average(time_series: pd.DataFrame,
                        rolling_settings: dict,
                        columns: Tuple[str, str],
                        title: str,
                        labels: Tuple[str, str, str],
                        to_plot: bool = False) -> matplotlib.axes.Axes:
    """
    Plot the moving average over time series

    Args:
        time_series: Pandas dataframe with time series
        rolling_settings: Dictionary containing rolling settings for moving average
        columns: Tuple of String name of columns in time_series for x-axis nad y-axis
        title: String title of the plot
        labels: Tuple of three strings containing labels for x-axis and y-axis and for the plot
        to_plot: Boolean indicating whether to plot or not

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
                                     y=moving_average.values,
                                     label=labels[2],
                                     ax=ax_time_series)

    logger.info('plot_moving_average - Set plot configurations')

    # Define legend settings
    ax_moving_average.legend(loc='upper center',
                             bbox_to_anchor=(0.5, 0.95),
                             fontsize=12,
                             ncol=2)

    # Switch for plotting or returning the axes
    if to_plot:
        logger.info('plot_regression_plot - Calling the plt.show()')

        # Show plt
        plt.show()

        # Define the layout
        plt.tight_layout()

    logger.info('plot_regression_plot - End')

    return ax_moving_average


def plot_lags_series(data: pd.Series,
                     number_lags: int,
                     nrows: int,
                     time_series_name: str) -> matplotlib.figure.Figure:
    """
    Plot a time series against a set of specific lag values with their correlation values

    Args:
        data: Pandas series with time series
        number_lags: Integer indicating number of lags to plot
        nrows: Integer indicating number of rows to plot
        time_series_name: String indicating name of the time series

    Returns:
        figure: Matplotlib figure object
    """
    logger.info('plot_lags_series - Start')

    # Compute the number of columns for the plot
    ncols = math.ceil(number_lags / nrows)

    # Plot settings
    plot_settings = {
        'nrows': nrows,
        'ncols': ncols,
        'figsize': (ncols * 2, nrows * 2 + 0.5),
    }

    # Define figure and axes
    figure, _ = plt.subplots(sharex=True, sharey=True, squeeze=False, **plot_settings)

    # Fetch the lags to plot
    for axis, lag_value in zip(figure.get_axes(), range(nrows * ncols)):
        # plot the lag
        axis = plot_single_lag(data, lag_value=lag_value + 1, ax=axis)

        # Set lag plot configurations
        axis.set_title(f"Lag {lag_value + 1}", fontdict={'fontsize': 14})
        axis.set(xlabel="", ylabel="")

    figure.suptitle(f'Lag Plot - {time_series_name}')

    # Set the layout
    figure.tight_layout(w_pad=0.1, h_pad=0.1)

    logger.info('plot_lags_series - End')

    return figure
