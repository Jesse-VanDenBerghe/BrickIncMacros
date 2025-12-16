
from PIL import Image
import numpy as np


def areImagesMatching(image1_path, image2_path, threshold=0.9):
    img1 = Image.open(image1_path).convert('RGB')
    img2 = Image.open(image2_path).convert('RGB')

    if img1.size != img2.size:
        return False

    arr1 = np.array(img1)
    arr2 = np.array(img2)

    matching_pixels = np.sum(np.all(arr1 == arr2, axis=-1))
    total_pixels = arr1.shape[0] * arr1.shape[1]

    similarity = matching_pixels / total_pixels
    return similarity >= threshold

def getColorAtPixel(image_path, x, y):
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    if x < 0 or x >= width or y < 0 or y >= height:
        raise ValueError("Coordinates are out of image bounds.")
    r, g, b = img.getpixel((x, y))
    return r, g, b

def areColorsMatching(color1, color2, tolerance=10):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def pixelMatchesColor(image_path, x, y, target_color, tolerance=10) -> bool:
    pixel_color = getColorAtPixel(image_path, x, y)
    return areColorsMatching(pixel_color, target_color, tolerance)
