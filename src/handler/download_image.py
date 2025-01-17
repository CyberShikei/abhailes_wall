import requests
import os


def download_image(file_path='images/image.jpg', url=None):
    """
    Downloads an image from a URL and saves it to a file.

    :param file_path: The path to save the image to.
    :param url: The URL of the image to download.
    :return: None
    """

    # Check if the file already exists
    if os.path.exists(file_path):
        msg = f"File {file_path} already exists. Skipping download."
        print(msg)
        return msg

    # Send a GET request to the URL
    response = requests.get(url)
    # Open a file in write-binary mode and save the image
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"Image saved to {file_path}")
