import pytest

from src.engine import set_wallpaper

TEST_DIR = "public/test_images/"


class TestSetWall():
    def test_set_wallpaper(self):
        path = TEST_DIR
        image = "test_image.jpg"
        fit = True

        assert set_wallpaper(
            f"{path}{image}", fit)

    def test_set_wallpaper_false_path(self):
        path = TEST_DIR
        image = "FAKE_FILE.jpg"

        try:
            assert not set_wallpaper(
                f"{path}{image}")
        except Exception as e:
            assert str(e) == "Image does not exist"


if __name__ == '__main__':
    pytest.main()
