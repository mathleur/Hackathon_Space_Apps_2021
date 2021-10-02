from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gen_lightcurve import gen_lightcurve
from runbatchfile import runBlender
#from brightness_calc1 import get_luminance
import time

def hello():
    print("Hello")

def getDirectory():
    global directory
    directory = filedialog.askdirectory()
    directory = directory.replace("/","\\")
    directoryEntry.delete(0,END)
    directoryEntry.insert(0, directory)
    print("Directory: ",directory)

def main():
    global x, brightnesses, directory   
    directoryString = directory
    runBlender(directoryString)
    print("Blender Run")
    x,brightnesses = gen_lightcurve(directoryString)

def createFigure():
    global x, brightnesses
    x = np.array(x)
    brightnesses = np.array(brightnesses)
    plotFigure.plot(x,brightnesses)


app = Tk()
app.title("ALCS")

frameLeft = Frame(master = app)
frameRight = Frame(master = app)

labelLeft = Label(master = frameLeft, text = "Left")
labelLeft.grid(row = 0, column = 0)



#directory = "C:\\Users"
directory = StringVar()
directoryEntry = Entry(master = frameLeft, textvariable = directory)
directoryEntry.grid(row=1,column = 1)

directoryButton = Button(master = frameLeft, text = "Choose Directory", command = getDirectory)
directoryButton.grid(row=1,column = 0)


periodLabel = Label(master = frameLeft, text = "Rotational Period")
periodLabel.grid(row=2,column = 0)

periodEntry = Entry(master = frameLeft)
periodEntry.grid(row=2,column = 1)

axisLabel = Label(master = frameLeft, text = "Rotational Axis")
axisLabel.grid(row=3,column = 0)

axisEntry = Entry(master = frameLeft)
axisEntry.grid(row=3,column = 1)



runButton = Button(master = frameLeft, text = "Run",command = main)
runButton.grid(row = 4, column = 0,columnspan = 2)






labelRight = Label(master = frameRight, text = "Right")
labelRight.grid(row = 0, column = 0)

#x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
#p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368, 19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

figureWindow = Figure(figsize=(6,6))
plotFigure = figureWindow.add_subplot(111)
#a.scatter(v,x,color='red')
#a.plot(p, range(2 +max(x)),color='blue')
#a.invert_yaxis()




x = []
brightnesses = []
#plotFigure.plot(x,brightnesses)

plotFigure.set_title ("Test Plot", fontsize=16)
plotFigure.set_ylabel("Y", fontsize=14)
plotFigure.set_xlabel("X", fontsize=14)

canvas = FigureCanvasTkAgg(figureWindow, master=frameRight)
canvas.get_tk_widget().grid(row = 1, column = 0)


#plt.plot(x, brightnesses)
#plt.savefig('E:\\Users\\John\\OneDrive\\Hackathon\\GithubFiles\\Space-Apps-Hackathon\\lightcurve.png')












frameLeft.pack(fill=BOTH, side=LEFT, expand=True)
frameRight.pack(fill=BOTH, side=RIGHT, expand=True)


app.mainloop()