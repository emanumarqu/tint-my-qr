#!/usr/bin/python3
from PIL import Image
from os import listdir
from os.path import isfile, join

# Change foreground
def new_fore(color):
    pass

# Change background
def new_back(color):
    pass

# Get images size
def get_image(img):
    img = 'inputs/' + img
    im = Image.open(img, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    print(width)
    print(height)

# Get QR codes
inputs = 'inputs/'
qr_codes = [f for f in listdir(inputs) if isfile(join(inputs, f))]

# Manipulate QR codes
for q in qr_codes:
    get_image(q)