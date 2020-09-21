"""Unit tests for src/logging_setup.py."""

import logging
import os
import sys

sys.path.append(os.path.join(os.getcwd(), "src"))

from logging_setup import configure_logger  # noqa


def test_configure_logger() -> None:
    """Tests the logger is imported correctly."""
    test_logger = configure_logger()
    assert isinstance(test_logger, logging.Logger)
