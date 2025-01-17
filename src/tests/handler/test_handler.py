import pytest
import os

from src.handler import download_image

TEST_IMAGE = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
IMAGE_PATH = "public/test_images/image_that_should_not_exist.jpg"


class TestHandler():
    def test_download_image(self):
        download_image(file_path=IMAGE_PATH,
                       url=TEST_IMAGE)

        assert os.path.exists(IMAGE_PATH)

    def test_download_image_exists(self):
        download_image(file_path=IMAGE_PATH,
                       url=TEST_IMAGE)

        assert download_image(file_path=IMAGE_PATH,
                              url=TEST_IMAGE) == f"File {IMAGE_PATH} already exists. Skipping download."
