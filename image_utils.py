import numpy as np
import cv2
from PIL import Image

def load_image(uploaded_file):
    """Convert uploaded image to OpenCV format."""
    image = Image.open(uploaded_file).convert("RGB")
    return np.array(image)

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
