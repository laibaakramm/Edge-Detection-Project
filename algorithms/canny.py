import cv2
from image_utils import to_grayscale

def apply_canny(image, params):
    gray = to_grayscale(image)
    sigma = params["sigma"]

    if sigma > 0:   
        gray = cv2.GaussianBlur(gray, (3, 3), sigma)

    edges = cv2.Canny(gray, params["lower"], params["upper"])
    return edges
