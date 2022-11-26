from PIL import Image
import PIL
import os
import glob

def compress(path):
    im = Image.open(path)