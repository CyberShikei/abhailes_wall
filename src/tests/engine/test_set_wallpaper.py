import pytest

from src.engine.set_wallpaper import set_wallpaper


class TestSetWall():
    def test_set_wallpaper(self):
        path = "public/images/"
        image = "test_image.jpg"
        fit = True

        assert set_wallpaper(
            f"{path}{image}", fit)

    def test_set_wallpaper_false_path(self):
        path = "public/images/"
        image = "FAKE_FILE.jpg"

        try:
            assert not set_wallpaper(
                f"{path}{image}")
        except Exception as e:
            assert str(e) == "Image does not exist"


if __name__ == '__main__':
    pytest.main()
