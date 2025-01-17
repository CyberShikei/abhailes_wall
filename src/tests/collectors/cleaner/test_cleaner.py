import pytest
import os

from src.collectors.cleaner import data_to_file, read_json

TEST_DATA = {'key': 'value'}

TEST_FILE = 'test_data.json'


class TestCleaner():
    def test_data_to_file(self):
        data = TEST_DATA

        assert data_to_file(data, TEST_FILE)

    def test_read_json(self):
        data = read_json(TEST_FILE)

        assert data == TEST_DATA

    def test_cleanup(self):
        # clean up
        os.remove(TEST_FILE)


if __name__ == '__main__':
    pytest.main()
