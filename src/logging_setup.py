"""Configure Logging."""

import logging
import logging.config

from yaml import safe_load


def configure_logger() -> logging.Logger:
    """Sets up & configures logger object.

    Returns:
        logging.Logger: [description]
    """
    with open("logging_config.yml", "r") as f:
        log_config = safe_load(f.read())

    logging.config.dictConfig(log_config)
    return logging.getLogger("standard")
