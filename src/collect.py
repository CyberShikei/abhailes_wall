# !venv/bin/python3
from collectors import APICollector

import pandas as pd

API_DATA = 'public/api_data.json'


def get_apod_data(start_date):
    api_data = pd.read_json(API_DATA, typ='series')

    url = api_data['api_url']
    endpoint = api_data['endpoint']
    params = api_data['params']

    params['start_date'] = start_date

    collector = APICollector(url, default_params=params)

    data = collector.get_data(endpoint, params)

    normal_data = pd.json_normalize(data)

    image_data = get_apod_images(normal_data)

    return image_data


def get_apod_images(data: pd.DataFrame):
    images = data[data['media_type'] == 'image']

    return images


def get_random_image(start_date):
    data = get_apod_data(start_date)

    return data.sample()
