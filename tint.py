#!/usr/bin/python3
from PIL import Image, 
from os import listdir
from os.path import isfile, join

# Save foreground & background pixels
def get_fore_back(img):
    # Store black pixels as foreground
    with Image.open(img) as im:
        px = im.load()
    px[4, 4] = (0, 0, 0)
    
    # Store remaining white pixels as background


    # return [f, b]
    return [[1, 2], [3, 4, 5]]

def set_fore_back(pixels, color):
    print(str(len(pixels)) + ' pixels will be changed to ' + str(color))

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