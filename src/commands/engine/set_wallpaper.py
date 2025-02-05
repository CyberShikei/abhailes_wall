import os
import sys
import subprocess


def __set_wallpaper_fit():
    """
    Set the wallpaper to fit the screen.
    """

    subprocess.run([
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-options",
        "scaled"
    ])

# TODO: Implement OS detection for Windows and MacOS


def set_wallpaper(image_path, fit=False):
    """
    Set the wallpaper to the image at the given path.

    :param image_path: The path to the image to set as the wallpaper.
    :param fit: Whether to fit the wallpaper to the screen.

    :return: True if the wallpaper was set successfully.
    """
    if not __does_picture_exist(image_path):
        raise Exception("Image does not exist")

    system = sys.platform
    if system.startswith("linux"):
        # Use gsettings to set the wallpaper
        try:
            subprocess.run([
                "gsettings",
                "set",
                "org.gnome.desktop.background",
                "picture-uri-dark",
                f"file://{os.path.abspath(image_path)}"
            ], check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to set wallpaper: {e}")
    else:
        raise Exception(f"Unsupported OS: {system}")

    if fit:
        __set_wallpaper_fit()

    return True


def __does_picture_exist(image_path):
    return os.path.exists(image_path)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        set_wallpaper(sys.argv[1])
    else:
        print("Usage: python set_wallpaper.py <path_to_image>")
