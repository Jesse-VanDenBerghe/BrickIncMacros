
from PIL import Image, ImageDraw
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
    return getColorAtPixelFromImage(img, x, y)

def getColorAtPixelFromImage(img, x, y):
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


def draw_centered_circle(image_path, output_path, center_coord, radius):
    """
    Opens an image, draws an orange circle centered at the given coordinates,
    and saves the result.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path where the modified image will be saved.
        center_coord (tuple): A tuple (x, y) representing the center of the circle.
        radius (int): The radius of the circle in pixels.
    """
    try:
        # 1. Open the existing image
        # .convert("RGBA") ensures compatible color modes if input is grayscale/indexed
        img = Image.open(image_path).convert("RGBA")
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return

    # 2. Create a drawing context on the image surface
    draw = ImageDraw.Draw(img)

    # 3. Define Orange Color (R, G, B, Alpha)
    # Alpha 255 means fully opaque.
    orange_color = (255, 165, 0, 255)

    # 4. Calculate the bounding box
    # Pillow draws ellipses inside a rectangle defined by:
    # [(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)]
    center_x, center_y = center_coord

    top_left_x = center_x - radius
    top_left_y = center_y - radius
    bottom_right_x = center_x + radius
    bottom_right_y = center_y + radius

    bounding_box = [
        (top_left_x, top_left_y),
        (bottom_right_x, bottom_right_y)
    ]

    # 5. Draw the ellipse (circle)
    # fill=color fills the inside, outline=color colors the border
    draw.ellipse(bounding_box, fill=orange_color, outline=orange_color)

    # 6. Save the result
    # Converting back to RGB before saving as JPEG is usually safer,
    # unless saving as PNG which supports RGBA.
    if output_path.lower().endswith(('.jpg', '.jpeg')):
         img = img.convert("RGB")

    img.save(output_path)
    print(f"Successfully saved image with orange circle to: {output_path}")
