import pytest

from src.collectors import APICollector

BASE_URL = "https://api.thecatapi.com/v1"


class TestApiCollector():
    def test_init(self):
        api = APICollector(BASE_URL)

        assert api.base_url == BASE_URL
        assert api.headers == {}
        assert api.default_params == {}

    def test_get_data(self):
        endpoint = "images/search"

        api = APICollector(BASE_URL)

        data = api.get_data(endpoint)

        assert data


if __name__ == '__main__':
    pytest.main()
