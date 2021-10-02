import numpy as np 
from brightness_calc1 import get_luminance
import matplotlib.pyplot as plt
import time

brightnesses = []
t1 = time.process_time()
for i in range(360):
    filename_beginning = 'C:\\Users\\Mathilde\\OneDrive\\Dokumente\\hackathon2021\\Pictures\\Image\\BlenderImage' + str(i) 
    filename = filename_beginning + '.png'
    brightnesses.append(get_luminance(filename))
    print(i)
brightnesses = np.asarray(brightnesses)

x = range(360)

plt.plot(x, brightnesses)
plt.savefig('C:\\Users\\Mathilde\\OneDrive\\Dokumente\\hackathon2021\\lightcurve.png')
t2 = time.process_time()
print(t2-t1)