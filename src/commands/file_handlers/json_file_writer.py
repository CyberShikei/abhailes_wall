# cleans json data (that has already been collected from an api)

import json


def write_json(json_string, file_name):
    """
    Writes JSON data to a file.

    Parameters:
        json_string (str): JSON data as a string.
        file_name (str): Name of the file to write the JSON data to.

    Returns:
        bool: True if the JSON data was successfully written to the file, False otherwise.
    """
    try:
        with open(file_name, "w") as file:
            json.dump(json_string, file)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
