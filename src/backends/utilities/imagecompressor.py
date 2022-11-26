from PIL import Image
import PIL
import os
import glob
from pathlib import Path

def compress(path):
    im = Image.open(path)
    print(f"The image size dimensions are: {im.size}")
    im.save(path,optimize=True,quality=30) 


def clean_directory(directory):
    files = os.listdir(directory)
    for file in files:
        compress(file)

def clear_images():
    parent = Path(Path.cwd()).parent
    directory = f"{parent}/images"
    for file in os.listdir(directory):
        compress(f"{parent}/images/{file}")

def clear_shop():
    parent = Path(Path.cwd()).parent
    directory = f"{parent}/shop"
    for f in glob.glob(directory, recursive=True):
        print(f)

if __name__ == "__main__":
    for f in glob.glob('../shop/**', recursive=True):
        print(f)