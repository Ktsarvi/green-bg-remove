# Green Screen Removal

A Python script that removes chromakey green backgrounds from images and exports them as transparent PNG assets.

## Features

- Automatic green screen detection using HSV color space
- Converts green background to transparent alpha channel
- Smooths edges to prevent jagged transparency borders
- Exports high-quality PNG with transparency

## Installation

Install the required dependencies:

```bash
pip install opencv-python numpy pillow
```

## Usage

1. Place your green screen image in the project directory as `image.png`
2. Run the script:

```bash
python script.py
```

3. The transparent output will be saved as `final_transparent_asset.png`

## Input Image Requirements

For best results, your input image must meet these **critical chromakey requirements**:

- **Background**: Solid, flat, uniform chromakey green color. Use EXACTLY hex color `#00FF00` (RGB 0, 255, 0). The entire background must be this single pure green color with NO variations, NO gradients, NO shadows, and NO atmospheric lighting effects.
- **White Outline**: The subject MUST have a clean, solid white outline/border (2–3 pixels wide) completely separating it from the green background. This border acts as a safety buffer to prevent color bleeding.
- **Clean Edges**: High-contrast, sharp, anti-aliased, and completely defined outer edges. No blurry details or atmospheric glow melting into the green background.
- **No Green on Subject**: The subject itself must not contain any pure chromakey green pixels.

## How It Works

1. Loads the image using OpenCV
2. Converts BGR color space to HSV for better color detection
3. Creates a binary mask targeting green pixels (Hue 35-85, Saturation 100-255, Value 100-255)
4. Inverts the mask to isolate the subject
5. Applies morphological operations to smooth edges
6. Merges RGB channels with the alpha transparency mask
7. Exports as a transparent PNG using PIL

## Customization

To process different files, modify the function call at the bottom of `script.py`:

```python
remove_green_screen("your_input.png", "your_output.png")
```

To adjust the green detection range, modify the HSV thresholds:

```python
lower_green = np.array([35, 100, 100])  # [Hue, Saturation, Value]
upper_green = np.array([85, 255, 255])
```
