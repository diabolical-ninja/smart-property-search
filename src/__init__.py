"""Configure Logging."""

import logging
import logging.config

from yaml import safe_load

logger = logging.getLogger(__name__)

with open("logging_config.yml", "r") as f:
    log_config = safe_load(f.read())

logging.config.dictConfig(log_config)

logger = logging.getLogger("standard")
