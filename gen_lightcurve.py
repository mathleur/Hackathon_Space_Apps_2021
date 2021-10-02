import numpy as np 
from brightness_calc1 import get_luminance
import matplotlib.pyplot as plt
import time

def gen_lightcurve(directoryStr):
    #global directory
    brightnesses = []
    t1 = time.process_time()
    for i in range(360):
        filename_beginning = directoryStr+'\\BlenderImage' + str(i) 
        filename = filename_beginning + '.png'
        brightnesses.append(get_luminance(filename))
        print(i)
    brightnesses = np.asarray(brightnesses)

    x = range(360)
    return x, brightnesses

# x, brightnesses = gen_lightcurve()
# plt.plot(x, brightnesses)
# plt.show()