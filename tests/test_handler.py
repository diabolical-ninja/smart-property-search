"""Unit tests for src/handler.py."""

import json
import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.join(os.getcwd(), "src"))

import handler  # noqa


success_test_files = os.listdir(os.path.join(Path(__file__).parent, "test_handler_payloads", "successes"))
failure_test_files = os.listdir(os.path.join(Path(__file__).parent, "test_handler_payloads", "failures"))


@pytest.mark.parametrize("test_file", success_test_files)
def test_search_success(test_file: dict) -> None:
    """Integration tests for successful smart search functionality.

    Notes:
        - Mocks lambda context with None (null)
        - Uses a sample event with all the fluff from API Gateway

    Args:
        test_file (dict): Sample payloads that should work successfully
    """
    with open(os.path.join(Path(__file__).parent, "test_handler_payloads", "successes", test_file)) as f:
        test_event = json.load(f)

    test_result = handler.search(test_event, None)
    assert isinstance(test_result, dict)
    assert test_result["statusCode"] == 200
    assert "body" in test_result


@pytest.mark.parametrize("test_file", failure_test_files)
def test_failures_success(test_file: dict) -> None:
    """Integration tests for unsuccessful smart search functionality.

    Notes:
        - Mocks lambda context with None (null)
        - Uses a sample event with all the fluff from API Gateway

    Args:
        test_file (dict): Sample payloads that should not
    """
    with open(os.path.join(Path(__file__).parent, "test_handler_payloads", "failures", test_file)) as f:
        test_event = json.load(f)

    test_result = handler.search(test_event, None)
    assert isinstance(test_result, dict)
    assert test_result["statusCode"] == 500
    assert "error" in test_result
