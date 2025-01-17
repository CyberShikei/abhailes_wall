# !venv/bin/python3
from .collectors import APICollector

import pandas as pd

from datetime import datetime

API_DATA = 'public/api_data.json'
CACHE_FILE = "cache/APOD_data.json"


def get_apod_data(start_date) -> pd.DataFrame:
    """
    Get APOD data from the API

    :param start_date: The date to start the search
    :return: A DataFrame with the APOD data
    """
    cache = __get_date_in_cache(start_date)
    if not cache.empty:
        return cache

    api_data = pd.read_json(API_DATA, typ='series')

    url = api_data['api_url']
    endpoint = api_data['endpoint']
    params = api_data['params']

    params['start_date'] = start_date

    collector = APICollector(url, default_params=params)

    data = collector.get_data(endpoint, params)

    # normal_data = pd.json_normalize(data)
    normal_data = pd.DataFrame(data)

    image_data = get_apod_images(normal_data)

    image_data.to_json(CACHE_FILE)

    return image_data


def get_apod_images(data: pd.DataFrame):
    images = data[data['media_type'] == 'image']

    return images


def get_random_image(start_date):
    data = get_apod_data(start_date)

    return data.sample()


def __get_cache_data():
    try:
        return pd.read_json(CACHE_FILE)
    except FileNotFoundError:
        return pd.DataFrame()


def __get_date_in_cache(date: datetime) -> pd.DataFrame:
    cache_data = __get_cache_data()
    if not cache_data.empty and date in cache_data['date']:
        # Get all the data from the cache from and after date
        return cache_data[cache_data['date'] >= date]
    else:
        return pd.DataFrame()
