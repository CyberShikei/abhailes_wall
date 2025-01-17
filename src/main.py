import pandas as pd

from APOD import get_apod_data
from datetime import datetime, timedelta


def main():
    date = "2025-01-01"
    data = get_apod_data(date)

    normalized_data = pd.json_normalize(data)

    print(normalized_data)


if __name__ == '__main__':
    main()
