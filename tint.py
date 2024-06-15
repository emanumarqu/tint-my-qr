#!/usr/bin/python3
from PIL import Image
from os import listdir
from os.path import join

# Improvements
# https://pillow.readthedocs.io/en/latest/reference/ImageFilter.html#PIL.ImageFilter.Filter
# https://pillow.readthedocs.io/en/latest/reference/ImageChops.html#PIL.ImageChops.difference
# add code from other repo to convert & validate hex/rgba inputs

# Create colorized copy of QR code
def create_color_copy(q, f, b):
    f = tuple(int(item) if item.isdigit()
        else item for item in f.split(' '))
    b = tuple(int(item) if item.isdigit()
        else item for item in b.split(' '))
    
    im = Image.open(q, 'r')
    pixdata = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            if pixdata[x, y] < (127, 127, 127, 127):
                pixdata[x, y] = f
            else:
                pixdata[x, y] = b
    im.save('outputs/' + q[7:])

# Get transformations
print('Enter colors as RGBA values: R G B A')
foreground = input('Foreground color: ')
background = input('Background color: ')

# Get QR codes
input_dir = 'inputs/'
qr_codes = [input_dir + f for f in listdir(input_dir) if join(input_dir, f).endswith('.png')]

# Process QR codes
for qrcode in qr_codes:
    create_color_copy(qrcode, foreground, background)