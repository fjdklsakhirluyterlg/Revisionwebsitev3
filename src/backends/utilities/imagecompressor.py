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

if __name__ == "__main__":
    parent = Path(Path.cwd()).parent
    print(parent)
    for file in f"{parent}/images":
        print(f"{parent}/images/{file}")