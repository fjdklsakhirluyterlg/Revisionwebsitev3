from PIL import Image
import PIL
import os
import glob

def compress(path):
    im = Image.open(path)
    print(f"The image size dimensions are: {im.size}")
    im.save(path,optimize=True,quality=30) 

file = "../images/nasa_pic.png"

compress(file)