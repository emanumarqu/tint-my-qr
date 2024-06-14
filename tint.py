#!/usr/bin/python3
from PIL import Image

# Change foreground
def new_fore(color):
    pass

# Change background
def new_back(color):
    pass

# Get images size
def get_image(img_path):
    im = Image.open(img_path, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())

