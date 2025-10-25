import cv2
import numpy as np
from image_utils import to_grayscale

def apply_sobel(image, params):
    gray = to_grayscale(image)
    ksize = params["ksize"]

    dx = dy = 0
    if params["direction"] == "X":
        dx, dy = 1, 0
    elif params["direction"] == "Y":
        dx, dy = 0, 1
    else:
        dx, dy = 1, 1

    sobel = cv2.Sobel(gray, cv2.CV_64F, dx, dy, ksize=ksize)
    abs_sobel = cv2.convertScaleAbs(sobel)
    return abs_sobel
