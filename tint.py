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
foreground = '1ecbe1' # foreground = input('Foreground color: ')
background = 'e1341e' # background = input('Background color: ')
for qrcode in qr_codes:
    process_qr(qrcode, foreground, background)