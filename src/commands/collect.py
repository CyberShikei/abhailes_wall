# !venv/bin/python3
from .collectors import APICollector
from .file_handlers import read_json, write_json

# import pandas as pd

import random
from datetime import datetime

API_DATA = 'public/api_data.json'
CACHE_FILE = "cache/APOD_data.json"
LAST_OUT_CACHE = "cache/wall.json"


def get_apod_data(start_date):
    """
    Get APOD data from the API

    :param start_date: The date to start the search
    :return: A DataFrame with the APOD data
    """
    cache = __get_date_in_cache(start_date)
    if not cache == {}:
        return cache

    api_data = read_json(API_DATA)

    url = api_data['api_url']
    endpoint = api_data['endpoint']
    params = api_data['params']

    params['start_date'] = start_date

    collector = APICollector(url, default_params=params)

    data = collector.get_data(endpoint, params)

    image_data = get_apod_images(data)

    write_json(image_data, CACHE_FILE)

    return image_data


def get_apod_images(data: dict):
    # obsolete images = data[data['media_type'] == 'image']
    images = []
    for entry in data:
        if entry['media_type'] == 'image':
            images.append(entry)

    return images


def get_random_image(start_date):
    data = get_apod_data(start_date)

    # obsolete return data.sample()

    random_index = random.randint(0, len(data) - 1)
    result = data[random_index]
    write_json(result, LAST_OUT_CACHE)

    return result


def __get_cache_data():
    try:
        return read_json(CACHE_FILE)
    except FileNotFoundError:
        return {}


def __get_date_in_cache(date: datetime):
    cache_data = __get_cache_data()
    if not cache_data == {} and date in __all_dates(cache_data):
        # Get all the data from the cache from and after date
        # obsolete return cache_data[cache_data['date'] >= date]
        return __get_after_date(date, cache_data)
    else:
        return {}


def __all_dates(data: list) -> list:
    dates = []
    for entry in data:
        dates.append(entry['date'])
    return dates


def __get_after_date(date: datetime, data: list):
    after_date = []
    for entry in data:
        if entry['date'] >= date:
            after_date.append(entry)
    return after_date
