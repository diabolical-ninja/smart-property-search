"""Unit tests for src/handler.py."""

import json
import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.join(os.getcwd(), "src"))

import handler  # noqa


test_files = os.listdir(os.path.join(Path(__file__).parent, "test_handler_payloads"))


@pytest.mark.parametrize("test_file", test_files)
def test_search(test_file: dict) -> None:
    """Integration tests for smart search functionality.
    
    Notes: 
        - Mocks lambda context with None (null)
        - Uses a sample event with all the fluff from API Gateway

    Args:
        test_file (dict): Sample payloads
    """
    with open(os.path.join(Path(__file__).parent, "test_handler_payloads", test_file)) as f:
        test_event = json.load(f)

    test_result = handler.search(test_event, None)
    assert isinstance(test_result, dict)
