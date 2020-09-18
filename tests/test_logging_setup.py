"""Unit tests for src/logging_setup.py."""

import logging

from src.logging_setup import configure_logger


def test_configure_logger() -> None:
    """Tests the logger is imported correctly."""
    test_logger = configure_logger()
    assert isinstance(test_logger, logging.Logger)
