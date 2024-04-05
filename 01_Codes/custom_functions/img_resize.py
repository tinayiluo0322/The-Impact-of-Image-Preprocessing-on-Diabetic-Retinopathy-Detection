"""
To resize the PIL image based on the inputs:
    - img: image to be resized
    - desired_size: desired size of final image
"""

from PIL import Image


def resize_image(img, desired_size=(512, 512)):
    # resizing the image
    new_img = img.resize(desired_size)
    return new_img
