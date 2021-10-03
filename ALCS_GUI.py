"""
This file creates a GUI window which enables the user to pass parameters to the program and generate a ligthcurve from them
"""

from pass_params import sentParams, save_dict_to_file
from tkinter import *
from tkinter import filedialog
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from gen_lightcurve import gen_lightcurve
from runbatchfile import runBlender
from tkinter.ttk import *
#from brightness_calc1 import get_luminance
import time
from tkinter import messagebox


def main():
    global x, brightnesses
    try:
        if int(entry2.get()) <1: 
            messagebox.showerror("Error", "Please check if number of steps is greater than 0")
        else:
            progress['value'] = 10
            app.update_idletasks()
            passparameters()
            progress['value'] = 30
            app.update_idletasks()
            runBlender()
            print("Blender Run")
            progress['value'] = 75
            app.update_idletasks()
            x,brightnesses = gen_lightcurve(int(entry2.get()))
            createFigure()
            progress['value'] = 100
            app.update_idletasks()
    except:
        messagebox.showerror("Error", "Please check if your input is in the right format")

def createFigure():
    global x, brightnesses
    # fig = Figure(figsize=(6,6))
    # a = fig.add_subplot(111)
    a.cla()
    x = np.asarray(x)
    x = 360 * x 
    x = x / (len(x)-1)
    period = int(entry6.get())
    x = x * period
    x = x / 360
    a.plot(x, brightnesses, color='blue')
    a.set_title ("Lightcurve", fontsize=16)
    a.set_ylabel("Brightness", fontsize=14)
    a.set_xlabel("Time in seconds", fontsize=14)
    # a.set_title ("Lightcurve", fontsize=16)
    # a.set_ylabel("Brightness", fontsize=14)
    # a.set_xlabel("Angle", fontsize=14)

    # canvas = FigureCanvasTkAgg(fig, master = frameRight)
    # canvas.get_tk_widget().pack()
    canvas.draw()

app = Tk()
app.title("ALCS")

frameLeft = Frame(master = app)
frameRight = Frame(master = app)

labelLeft = Label(master = frameLeft, text = "Insert your variables here!")
labelLeft.config(font=('Times New Roman', 28, 'bold'))
labelLeft.grid(row = 0, column = 0, columnspan = 2, pady = 25)


def passparameters():
    # global entry1, entry2, entry3, entry4, entry5
    cam = entry1.get()
    cam = tuple(map(float, cam.split(", ")))
    steps = int(entry2.get())
    rot = entry3.get()
    rot = tuple(map(float, rot.split(", ")))
    filename = entry4.get()
    light = int(entry5.get())
    print(cam)
    save_dict_to_file(sentParams(cam, steps, rot, filename, light))


camLabel = Label(master=frameLeft,
                 text="Camera position (3-position tuple)", font= ('​Times New Roman', 12, 'bold'))
camLabel.grid(row=1, column=0)
camLabel = Label(master=frameLeft,
                 text="eg: 10, 0, 0 with a space after the comma")
camLabel.grid(row=2, column=0, pady=(0, 10))

entry1 = Entry(master=frameLeft)
entry1.grid(row=1, column=1)

stepsLabel = Label(master=frameLeft, text="Number of steps (integer)", font= ('​Times New Roman', 12, 'bold'))
stepsLabel.grid(row=3, column=0)
stepsLabel = Label(master=frameLeft, text="eg: 3")
stepsLabel.grid(row=4, column=0, pady=(0, 10))

entry2 = Entry(master=frameLeft)
entry2.grid(row=3, column=1)

rotLabel = Label(master=frameLeft, text="Rotational axis (3-position tuple)", font= ('​Times New Roman', 12, 'bold'))
rotLabel.grid(row=5, column=0)
rotLabel = Label(master=frameLeft, text="eg: 0, 0, 1 with a space after the comma")
rotLabel.grid(row=6, column=0, pady=(0, 10))

entry3 = Entry(master=frameLeft)
entry3.grid(row=5, column=1)

fileLabel = Label(master=frameLeft, text="Filename (string)", font= ('​Times New Roman', 12, 'bold'))
fileLabel.grid(row=7, column=0)
fileLabel = Label(master=frameLeft, text="eg: 1996hw1.obj ")
fileLabel.grid(row=8, column=0, pady=(0, 10))

entry4 = Entry(master=frameLeft)
entry4.grid(row=7, column = 1)

lightLabel = Label(master=frameLeft, text="Light angle (integer)", font= ('​Times New Roman', 12, 'bold'))
lightLabel.grid(row=9, column=0)
lightLabel = Label(master=frameLeft, text="eg: 60 ")
lightLabel.grid(row=10, column=0, pady=(0, 10))

entry5 = Entry(master=frameLeft)
entry5.grid(row=9, column = 1)

periodLabel = Label(master=frameLeft, text="Rotation Period (integer) in seconds", font= ('​Times New Roman', 12, 'bold'))
periodLabel.grid(row=11, column=0)
periodLabel = Label(master=frameLeft, text="eg: 12 ")
periodLabel.grid(row=12, column=0, pady=(0, 0))

entry6 = Entry(master=frameLeft)
entry6.grid(row=11, column = 1)

runButton = Button(master= frameLeft, text = "Run", command = main)
runButton.grid(row=16, column=0, columnspan=2, pady = (35, 15))

button_quit = Button(master=frameLeft, text="Exit Program", command=app.quit)
button_quit.grid(row=13, column=0, columnspan=2, pady=25)

ProgressLabel = Label(master=frameLeft, text="Progress made", font= ('​Times New Roman', 12, 'bold'))
ProgressLabel.grid(row=14, column=0, columnspan=2, pady=(25, 0))
progress = Progressbar(master=frameLeft, orient=HORIZONTAL,
                       length=300, mode='determinate')
progress.grid(row=15, column=0, columnspan=2, pady=(0, 25), padx=50)

fig=Figure(figsize=(9, 7.5),dpi=110)
a=fig.add_subplot(111)

canvas=FigureCanvasTkAgg(fig, master = frameRight)
canvas.draw()
canvas.get_tk_widget().grid(row=30,column=0,sticky="wn",padx=5)

a.set_title ("Lightcurve", fontsize=16)
a.set_ylabel("Brightness", fontsize=14)
a.set_xlabel("Angle", fontsize=14)
a.grid()

frameLeft.pack(fill=BOTH, side=LEFT, expand=True)
frameRight.pack(fill=BOTH, side=RIGHT, expand=True)

app.mainloop()
