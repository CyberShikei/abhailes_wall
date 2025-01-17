import pytest

from src.collect import get_apod_data


class TestAPOD():
    def test_get_apod_data(self):
        start_date = '2025-01-01'

        data = get_apod_data(start_date)

        assert data


if __name__ == '__main__':
    pytest.main()
