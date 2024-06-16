"""
The module contains several util functions for performing exploratory data analysis.
"""
import matplotlib.pyplot as plt
# Import Standard Libraries
import numpy as np
import os
from pathlib import Path
import pandas as pd
import matplotlib
import seaborn as sns
from typing import Tuple

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
                     x_column: str,
                     y_column: str,
                     title: str,
                     labels: Tuple[str, str, str]) -> matplotlib.axes.Axes:
    """
    Plots a time series using seaborn matplotlib Axes.

    Args:
        time_series: Pandas dataframe with time series
        x_column: String name of column in time_series for x-axis
        y_column: String name of column in time_series for y-axis
        title: String title of plot
        labels: Tuple of three strings containing labels for x-axis and y-axis and for the plot

    Returns:
        ax: matplotlib Axes
    """
    # Plot the data
    ax = sns.lineplot(data=time_series,
                      x=time_series[x_column],
                      y=time_series[y_column],
                      label=labels[2])

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

    # Show plt
    plt.show()

    # Define the layout
    plt.tight_layout()

    return ax


def plot_predictions_vs_time_series(time_series: pd.DataFrame,
                                    predictions: np.ndarray,
                                    x_column: str,
                                    y_column: str,
                                    title: str,
                                    labels: Tuple[str, str]) -> matplotlib.axes.Axes:
    # Retrieve time series plot
    ax_time_series = plot_time_series(time_series=time_series,
                                      x_column=x_column,
                                      y_column=y_column,
                                      title=title,
                                      labels=labels)

    # Plot predictions
    ax_predictions = sns.lineplot(x=time_series[x_column],
                                  y=predictions,
                                  ax=ax_time_series)

    ax_predictions.legend(handles=[ax_time_series, ax_predictions],
                          labels=['Times Series', 'Predictions'])

    return ax_predictions
