#!/usr/bin/python3
from PIL import Image
from os import listdir
from os.path import join

# Identify foreground & background pixels
# def get_fore_back(pixels):

    # Store black pixels as foreground
    
    # Store remaining white pixels as background

    # return [f, b]
 
# Change pixels' colors
def set_fore_back(pixels, color):
    print(str(len(pixels)) + ' pixels will be changed to ' + str(color))
    for p in pixels:
        print(p)

# Process image
def process_qr(q, f, b):
    im = Image.open(q, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    
    print(len(pixel_values))
    fore_back = get_fore_back(pixel_values)
    
    # if f != '':
    #     set_fore_back(fore_back[0], f)
    # if b != '':
    #     set_fore_back(fore_back[1], b)

# Get QR codes
input_dir = 'inputs/'
qr_codes = [input_dir + f for f in listdir(input_dir) if join(input_dir, f).endswith('.png')]
print(qr_codes)

# Get transformations
print('Enter colors as RGBA tuples --> (0, 100, 255, 0.5)')
# 
# add code from other repo to convert hex values to rgba
# and validates rgba input
# 
foreground = (30, 203, 225, 1)
# background = (225, 52, 30, 0.5)
# foreground = input('Foreground color: ')
background = input('Background color: ')
print('\n')

# Process QR codes
for qrcode in qr_codes:
    process_qr(qrcode, foreground, background)

# Improvements
# https://pillow.readthedocs.io/en/latest/reference/ImageFilter.html#PIL.ImageFilter.Filter
# https://pillow.readthedocs.io/en/latest/reference/ImageChops.html#PIL.ImageChops.difference