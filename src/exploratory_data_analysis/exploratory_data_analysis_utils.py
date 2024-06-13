"""
The module contains several util functions for performing exploratory data analysis.
"""
# Import Standard Libraries
import os
from pathlib import Path
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


# TODO: Refactor using Seaborn lineplot and all usual "prettienes"
def plot_time_series(time_series: pd.DataFrame, x_column: str, y_column: str, title: str) -> matplotlib.axes.Axes:
    plot_params = dict(
        color="0.75",
        style=".-",
        markeredgecolor="0.25",
        markerfacecolor="0.25",
        legend=False,
    )

    ax = sns.lineplot(data=time_series,
                      x=time_series[x_column],
                      y=time_series[y_column])

    # Set title
    ax.set_title(title,
                 fontsize=20)
    # Set tick rotation
    ax.tick_params(labelrotation=45)

    return ax
