#!/usr/bin/python3
from PIL import Image
from os import listdir
from os.path import isfile, join

# Save foreground & background pixels
def get_fore_back(img):
    return [34, 69]

def set_fore_back(pixels, color):
    pass

# Process image
def process_qr(q, f, b):
    im = Image.open(q, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    
    im_fb = get_fore_back(q)
    if f != '':
        set_fore_back(im_fb[0], f)
    if b != '':
        set_fore_back(im_fb[1], b)

# Get QR codes
input_dir = 'inputs/'
qr_codes = [input_dir + f for f in listdir(input_dir) if isfile(join(input_dir, f))]

# Process QR codes
print('Enter colors as RGBA tuples --> (0, 100, 255, 0.5)')
# add code from other repo to convert hex values to rgba
foreground = (30, 203, 225, 1)
# background = (225, 52, 30, 0.5)
# foreground = input('Foreground color: ')
background = input('Background color: ')
for qrcode in qr_codes:
    process_qr(qrcode, foreground, background)