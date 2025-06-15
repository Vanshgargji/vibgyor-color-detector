import numpy as np
import cv2
from PIL import Image

def load_and_prepare_image(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    height, width = image_cv.shape[:2]
    if width > 800:
        scale = 800 / width
        image_cv = cv2.resize(image_cv, (int(width * scale), int(height * scale)))

    hsv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2HSV)
    return image_cv, hsv
