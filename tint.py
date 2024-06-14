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


# Create colorized copy of QR code
def create_color_copy(q, f, b):
    im = Image.open(q, 'r')
    
    pixdata = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            if pixdata[x, y] == (0, 0, 0, 255) or pixdata[x, y] == (0, 0, 1, 255):
                pixdata[x, y] = f
            else:
                pixdata[x, y] = b

    im.show()
    # im.save('outputs/')

# Get QR codes
input_dir = 'inputs/'
qr_codes = [input_dir + f for f in listdir(input_dir) if join(input_dir, f).endswith('.png')]

# Get transformations
print('Enter colors as RGBA tuples --> (0, 100, 255, 0.5)')
# 
# add code from other repo to convert hex values to rgba
# and validates rgba input
# 
foreground = (30, 203, 225, 255)
background = (225, 52, 30, 50)
# foreground = input('Foreground color: ')
# background = input('Background color: ')
print('\n')

# Process QR codes
for qrcode in qr_codes:
    create_color_copy(qrcode, foreground, background)

# Improvements
# https://pillow.readthedocs.io/en/latest/reference/ImageFilter.html#PIL.ImageFilter.Filter
# https://pillow.readthedocs.io/en/latest/reference/ImageChops.html#PIL.ImageChops.difference