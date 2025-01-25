import os


def save_image(url_response, path, overwrite=False):
    """Save an image to a file.

    Args:
        image (np.ndarray): The image to save.
        path (str): The path to save the image to.
    """
    # if file already exists ask if it should be overwritten
    if not overwrite:
        if os.path.exists(path):
            return None
    # save image response to file
    with open(path, 'wb') as file:
        file.write(url_response.content)
        print(f"Image saved to {path}")
