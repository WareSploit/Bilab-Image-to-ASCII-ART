from PIL import Image
import numpy as np
import os
import glob
import sys

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def convert_to_ascii(image_path, height=50):
    if not os.path.exists(image_path):
        return "Image not found"

    try:
        img = Image.open(image_path).convert("L")
    except Exception:
        return "Failed to load image"

    width, old_height = img.size
    aspect_ratio = width / old_height
    new_width = int(height * aspect_ratio * 1.1)
    
    img = img.resize((new_width, height))
    pixels = np.array(img)
    char_indices = (pixels / 255 * (len(ASCII_CHARS) - 1)).astype(int)
    
    ascii_art = ""
    for row in char_indices:
        ascii_art += "".join(ASCII_CHARS[i] for i in row) + "\n"
        
    return ascii_art

def main():
    # Логика запуска: либо из аргументов, либо поиск в assets
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        assets_folder = "assets"
        extensions = ['*.png', '*.jpg', '*.jpeg', '*.webp']
        image_path = None
        for ext in extensions:
            files = glob.glob(os.path.join(assets_folder, ext))
            if files:
                image_path = files[0]
                break

    if image_path:
        result = convert_to_ascii(image_path, height=50)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(result)
    else:
        print("No image found in assets folder or provided path.")

if __name__ == "__main__":
    main()