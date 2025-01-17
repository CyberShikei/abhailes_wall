from collect import get_random_image
from handler import download_image
from engine import set_wallpaper

import datetime

IMAGES_PATH = 'images/'


def main():
    # data = get_random_image(date)
    today = datetime.datetime.today()
    date = today.strftime("%Y-%m-%d")
    img_type = ""
    while img_type != 'image':
        data = get_random_image(date)

        if img_type != "":
            print("Image not found, trying another date")
        today -= datetime.timedelta(days=1)
        date = today.strftime("%Y-%m-%d")
        img_type = data.iloc[0]['media_type']

    img_data = (img_name,
                img_url,
                img_date,
                img_desc) = __get_image_data(data)

    print(f"Downloading image: {img_data}")

    download_image(img_name, img_url)

    set_wallpaper(img_data[0])


def __get_image_data(data):
    image_name = data.iloc[0]['title']
    image_name = image_name.replace(" ", "_") + '.jpg'
    image_path = IMAGES_PATH + image_name
    image_url = data.iloc[0]['hdurl']
    image_date = data.iloc[0]['date']
    image_desc = data.iloc[0]['explanation']

    return (image_path, image_url, image_date, image_desc)


if __name__ == '__main__':
    main()
