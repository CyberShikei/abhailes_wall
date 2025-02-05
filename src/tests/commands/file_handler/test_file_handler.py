import pytest
import os

from src.commands import write_json, read_json

TEST_DATA = {'key': 'value'}

TEST_FILE = 'test_data.json'


class TestCleaner():
    def test_data_to_file(self):
        data = TEST_DATA

        assert write_json(data, TEST_FILE)

    def test_read_json(self):
        data = read_json(TEST_FILE)

        assert data == TEST_DATA

    def test_cleanup(self):
        # clean up
        os.remove(TEST_FILE)


if __name__ == '__main__':
    pytest.main()
