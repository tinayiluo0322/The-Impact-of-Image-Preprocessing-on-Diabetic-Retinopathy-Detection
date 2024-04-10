"""
To crop the image based on the inputs:
    - img: image to be cropped
    - desired_size: desired size of final image
    - threshold: threshold value to be used for each pixel
"""

import numpy as np
from PIL import Image


def crop_image(img, threshold=15, resize_flag=False, desired_size=(512, 512)):
    # Convert image to numpy array
    img_np = np.array(img)

    # Get the shape of the image
    x_dim = img_np.shape[0]
    y_dim = img_np.shape[1]

    # Sum along the color axis (assuming the color axis is the third dimension)
    pixel_sums = img_np.sum(axis=2)

    # Sum along the x and y axes
    x_arr = pixel_sums.sum(axis=1)
    y_arr = pixel_sums.sum(axis=0)

    # Find the first and last indices where the sum exceeds the threshold
    x_start = np.where(x_arr > threshold * y_dim)[0][0]
    x_end = np.where(x_arr > threshold * y_dim)[0][-1]

    y_start = np.where(y_arr > threshold * x_dim)[0][0]
    y_end = np.where(y_arr > threshold * x_dim)[0][-1]

    # Crop the image
    new_img = img_np[x_start:x_end, y_start:y_end]

    # converting back to image
    new_img = Image.fromarray(new_img)

    # resizing the image
    if resize_flag:
        new_img = new_img.resize(desired_size)

    return new_img
