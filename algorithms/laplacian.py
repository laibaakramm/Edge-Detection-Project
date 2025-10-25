import cv2
from image_utils import to_grayscale

def apply_laplacian(image, params):
    gray = to_grayscale(image)
    ksize = params["ksize"]
    laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
    return cv2.convertScaleAbs(laplacian)
