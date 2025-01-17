import json


def read_json(file_path) -> dict:
    """
    Read JSON data from a file.

    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.

    Raises:
        ValueError: If no file path is provided.
        FileNotFoundError: If the file is not found.
        Exception: If an error occurs while reading the file.
    """
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
