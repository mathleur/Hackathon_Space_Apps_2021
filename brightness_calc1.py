from PIL import Image
from math import sqrt
import numpy as np
import time


def get_luminance(filename):
    im = Image.open(filename)
    arr = np.array(im)
    R = arr[:,:,0]
    G = arr[:,:,1]
    B = arr[:,:,2]
    luminance = (0.2126*R) + (0.7152*G) + (0.0722*B)
    luminance = np.mean(luminance)
    return luminance

# t1 = time.process_time()
# L = get_luminance("BlenderImage0.png") 
# t2 = time.process_time()
# print(L)
# print(t2-t1)