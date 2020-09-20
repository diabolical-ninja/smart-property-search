"""Unit tests for src/utils.py."""

from datetime import date, datetime

import pytest

from utils import chunks, extend_dictionary, json_serial


class TestJsonSerial:
    """Tests the json_serial function."""

    def test_json_serial(self) -> None:
        """Tests for correct output."""
        assert json_serial(date(2020, 1, 1)) == "2020-01-01"
        assert json_serial(datetime(2020, 1, 1, 10, 9, 8)) == "2020-01-01T10:09:08"

    def test_serialisation_error(self) -> None:
        """Test for non-datetime objects."""
        with pytest.raises(TypeError):
            json_serial("hello world")
        with pytest.raises(TypeError):
            json_serial(123)


class TestChunks:
    """Tests the chunks function."""

    def test_chunks(self) -> None:
        """Tests chunks are of the correct size."""
        test_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for item in chunks(test_list, 4):
            assert len(item) <= 4

        for item in chunks(test_list, 50):
            assert len(item) <= 50


class TestExtendDictionary:
    """Tests the extend_dictionary function."""

    def setup_class(self) -> None:
        """Initialises sample dicts for testing."""
        self.dictionary_one = {"a": 1}
        self.dictionary_two = {"b": 2}

    def test_extend_dictionary(self) -> None:
        """Check extension functionality is working correctly."""
        output = extend_dictionary(self.dictionary_one, self.dictionary_two, "b")

        assert type(output) == dict
        assert "b" in output
        assert list(output.keys()) == ["a", "b"]

    def test_key_overwrite_warning(self) -> None:
        """Check the corect warning is being shown."""
        with pytest.warns(UserWarning) as record:
            extend_dictionary(self.dictionary_one, self.dictionary_two, "a")

            assert len(record) == 1
            assert record[0].message.args[0] == "Key 'a' already exists and will be overwritten"
