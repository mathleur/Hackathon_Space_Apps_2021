# need to install Pillow package
# calculates brightness of an image as the average luminance of the pixels in the image

from PIL import Image
from math import sqrt
import numpy as np


def get_luminance(filename):
    im = Image.open(filename)
    #coordinates of the pixel
    width, height = im.size
    luminances = []
    for X in range(width):
        for Y in range(height):
            #Get RGB
            pixelRGB = im.getpixel((X,Y))
            R,G,B,A = pixelRGB 
            luminance1 = (0.2126*R) + (0.7152*G) + (0.0722*B)
            luminances.append(luminance1)
    luminances = np.asarray(luminances)
    luminance = np.mean(luminances)
    return luminance


# L = get_luminance("cat1test.jpg") 
# print(L)
