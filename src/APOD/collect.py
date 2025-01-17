# !venv/bin/python3
from src.collectors import APICollector
from src.cleaner import read_json

API_DATA = 'public/api_data.json'


def get_apod_data(start_date):
    api_data = read_json(API_DATA)

    url = api_data['api_url']
    endpoint = api_data['endpoint']
    params = api_data['params']

    collector = APICollector(url, default_params=params)

    data = collector.get_data(endpoint, params)

    return data
