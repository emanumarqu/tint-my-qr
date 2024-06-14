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

# Process image
def process_qr(q, f, b):
    im = Image.open(q, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())

# Get QR codes
input_dir = 'inputs/'
qr_codes = [input_dir + f for f in listdir(input_dir) if isfile(join(input_dir, f))]

# Process QR codes
print('Enter colors as RGBA tuples like (0, 255, 100, 0.5)')
# add code from other repo to convert hex values to rgba
foreground = (30, 203, 225, 1) # foreground = input('Foreground color: ')
background = (225, 52, 30, 0.5) # background = input('Background color: ')
for qrcode in qr_codes:
    process_qr(qrcode, foreground, background)