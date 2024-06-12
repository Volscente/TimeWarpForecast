"""
The module contains several general util functions
"""
# Import Standard Libraries
import os
from pathlib import Path
import pandas as pd
import yaml


# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def read_configuration(file_name: str) -> dict:
    """
    Read and return the specified configuration file from the 'configuration' folder

    Args:
        file_name: String configuration file name to read

    Returns:
        configuration: Dictionary configuration
    """

    logger.info('read_configuration - Start')

    try:

        logger.info('read_configuration - Reading %s', file_name)

        # Read configuration file
        with open(Path(__file__).parents[2] / 'configuration' / file_name,
                  encoding='utf-8') as config_file:

            configuration = yaml.safe_load(config_file.read())

    except FileNotFoundError as exc:

        raise FileNotFoundError(f'read_data - File {file_name} not found') from exc

    logger.info('read_configuration - Configuration file %s read successfully', file_name)

    logger.info('read_configuration - End')

    return configuration


def build_path_from_list(path_list: list) -> Path:
    """
    Build absolute pathlib.Path from relative path list from project root

    Args:
        path_list: List of relative path from root

    Returns
        absolute_path: pathlib.Path absolute path
    """
    logger.info('build_path_from_list - Start')
    logger.info('build_path_from_list - Retrieve root path to the project folder')

    # Retrieve root path
    root_path = Path(__file__).parents[2]

    # Initialise the returned absolute path
    absolute_path = root_path

    logger.info('build_path_from_list - Build the absolute path')

    # Build the absolute path to the target folder/file
    for folder in path_list:

        # Add the folder to the absolute path
        absolute_path = absolute_path / folder

    logger.info('build_path_from_list - End')

    return absolute_path


def read_data_from_config(data_config: dict) -> pd.DataFrame:
    """
    Read data as a Panda DataFrame from a dictionary configuration with structure

        <data_config_name>:
            data_path: list[str]
            date_columns: list[str]
            delimiter: str

    Args:
        data_config: Dictionary of data configuration

    Returns:
        data: Panda DataFrame read from configuration
    """

    logger.info('read_data_from_config - Start')

    logger.info('read_data_from_config - Retrieve data path')

    # Retrieve data path
    data_path = build_path_from_list(data_config['data_path'])

    # Check if the data_path exists
    if not data_path.exists():

        raise FileNotFoundError(f'read_data_from_config - {data_path} not found')

    logger.info('read_data_from_config - Retrieved data path %s', data_path.as_posix())

    logger.info('read_data_from_config - Reading data')

    # Read data with Pandas
    data = pd.read_csv(data_path,
                       sep=data_config['delimiter'],
                       parse_dates=data_config['date_columns'])

    logger.info('read_data_from_config - Successfully read data with %s rows and %s columns',
                len(data), len(data.columns))

    logger.info('read_data_from_config - End')

    return data
