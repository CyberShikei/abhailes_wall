import requests
# import os


def download_image(file_path='images/image.jpg', url=None):
    """
    Downloads an image from a URL and saves it to a file.

    :param file_path: The path to save the image to.
    :param url: The URL of the image to download.
    :return: None
    """
    # Send a GET request to the URL
    response = requests.get(url)
    return response
