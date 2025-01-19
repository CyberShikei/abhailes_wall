import datetime

from .engine import set_wallpaper
from .data_handler import download_image, get_image_data
from .collect import get_random_image


def set_wall_to_apod(date_in: str):
    date = check_date(date_in)

    print(date)
    img_type = ""
    while img_type != 'image':
        data = get_random_image(date)

        if img_type != "":
            print(f"Image not found, trying the day before {date} date")

        date = adjust_date(date, 1)
        img_type = data.iloc[0]['media_type']

    img_data = (img_name,
                img_url,
                img_date,
                img_desc) = get_image_data(data)

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
