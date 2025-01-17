import pandas as pd

from collect import get_apod_data
from engine import set_wallpaper


def main():
    date = "2025-01-01"
    data = get_apod_data(date)

    print(data)


if __name__ == '__main__':
    main()
