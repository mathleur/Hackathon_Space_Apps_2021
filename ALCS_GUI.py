from tkinter import *
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from brightness_calc1 import get_luminance
import time

app = Tk()

frameLeft = Frame(master = app)
frameRight = Frame(master = app)

labelLeft = Label(master = frameLeft, text = "Left")
labelLeft.grid(row = 0, column = 0)

labelRight = Label(master = frameRight, text = "Right")
labelRight.grid(row = 0, column = 0)

x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368, 19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

fig = Figure(figsize=(6,6))
a = fig.add_subplot(111)
a.scatter(v,x,color='red')
a.plot(p, range(2 +max(x)),color='blue')
a.invert_yaxis()

a.set_title ("Test Plot", fontsize=16)
a.set_ylabel("Y", fontsize=14)
a.set_xlabel("X", fontsize=14)

canvas = FigureCanvasTkAgg(fig, master=frameRight)
canvas.get_tk_widget().grid(row = 1, column = 0)



#Light Curve
brightnesses = []
t1 = time.process_time()
for i in range(360):
    filename_beginning = 'E:\\Users\\John\\OneDrive\\Hackathon\\GithubFiles\\Space-Apps-Hackathon\\BlenderImage' + str(i) 
    filename = filename_beginning + '.png'
    brightnesses.append(get_luminance(filename))
    print(i)
brightnesses = np.asarray(brightnesses)

x = range(360)

#plt.plot(x, brightnesses)
#plt.savefig('E:\\Users\\John\\OneDrive\\Hackathon\\GithubFiles\\Space-Apps-Hackathon\\lightcurve.png')
t2 = time.process_time()
print(t2-t1)











frameLeft.pack(fill=BOTH, side=LEFT, expand=True)
frameRight.pack(fill=BOTH, side=RIGHT, expand=True)
app.mainloop()