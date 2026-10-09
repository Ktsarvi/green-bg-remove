import cv2
import numpy as np
from PIL import Image


def remove_green_screen(image_path, output_path):
    # Load image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not load image from {image_path}")

    # Convert BGR to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Target pure chromakey green (#00FF00 -> Hue ~60 deg, 100% Sat, 100% Val)
    # OpenCV Hue range is 0-180 (60 deg -> 30)
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    # Create binary mask (green = 255, subject = 0)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Invert mask so subject = 255, background = 0
    subject_mask = cv2.bitwise_not(green_mask)

    # Smooth edges slightly to prevent jagged transparency borders
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    subject_mask = cv2.morphologyEx(subject_mask, cv2.MORPH_CLOSE, kernel)

    # Convert BGR to RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Split RGB channels and attach the transparency (Alpha) channel
    r, g, b = cv2.split(rgb_img)
    rgba_image = cv2.merge([r, g, b, subject_mask])

    # Export as transparent PNG
    pil_img = Image.fromarray(rgba_image)
    pil_img.save(output_path, "PNG")
    print(f"Success! Saved transparent asset to: {output_path}")


# Run pipeline
remove_green_screen("image.png", "final_transparent_asset.png")
