import datetime
import os

from .engine import set_wallpaper
from .data_handler import download_image, get_image_data
from .collect import get_random_image

CACHE_DESCRIPTION = "cache/description.txt"


def set_wall_to_apod(date_in: str):
    date = check_date(date_in)

    print(date)
    # while img_type != 'image':
    data = get_random_image(date)
    print(data)

    # if img_type != "":
    #    print(f"Image not found, trying the day before {date} date")

    # date = adjust_date(date, 1)
    # img_type = data['media_type']

    img_data = (img_name,
                img_url,
                img_date,
                img_desc,
                img_title) = get_image_data(data)

    __create_description_file(img_data)

    # if image file does not exisst download it
    if not os.path.exists(img_name):
        print(f"Downloading image: {img_data[0:3]}")

        download_image(img_name, img_url)

    set_wallpaper(img_data[0])


def check_date(date):
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    if isinstance(date, datetime.datetime):
        date = date.date()
    elif isinstance(date, datetime.date):
        return date
    else:
        raise TypeError("Date must be a string or datetime object")

    return date


def adjust_date(date, days):
    new_date = check_date(date)
    # Adjust the date
    new_date -= datetime.timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")


def __create_description_file(image_data):
    name, desc, date = image_data[4], image_data[3], image_data[2]

    res = f"{name} | {date} | {desc} | "

    with open(CACHE_DESCRIPTION, "w") as file:
        file.write(res)
