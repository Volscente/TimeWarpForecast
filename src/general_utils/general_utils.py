"""
The module contains several general util functions
"""
# Import Standard Libraries
import os
from pathlib import Path
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
