import json


def read_json(file_path) -> dict:
    if file_path is None:
        raise ValueError("No file path provided.")

    # get data from json file as a dictionary
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

    return data
