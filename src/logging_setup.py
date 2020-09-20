"""Configure Logging."""

import logging
import logging.config
import os

from yaml import safe_load


def configure_logger() -> logging.Logger:
    """Sets up & configures logger object.

    Returns:
        logging.Logger: Configured logger
    """
    config_file = os.path.join(os.path.dirname(__file__), "logging_config.yml")
    with open(config_file, "r") as f:
        log_config = safe_load(f.read())

    logging.config.dictConfig(log_config)
    return logging.getLogger("standard")
