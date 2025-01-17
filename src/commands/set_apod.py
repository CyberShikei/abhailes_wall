import datetime

from .engine import set_wallpaper
from .data_handler import download_image, get_image_data
from .collect import get_random_image


def set_wall_to_apod(date: str):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    img_type = ""
    while img_type != 'image':
        data = get_random_image(date)

        if img_type != "":
            print(f"Image not found, trying the day before {date} date")
        date -= datetime.timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
        img_type = data.iloc[0]['media_type']

    img_data = (img_name,
                img_url,
                img_date,
                img_desc) = get_image_data(data)

    print(f"Downloading image: {img_data}")

    download_image(img_name, img_url)

    set_wallpaper(img_data[0])
