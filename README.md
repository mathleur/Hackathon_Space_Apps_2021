# Hackathon_Space_Apps_2021

## How to use this repository

### Prerequisites
Install the Blender application under the path "C:\Program Files\Blender Foundation\Blender 2.93\blender.exe".
<br>
Or if the Blender application was installed under another path, change the path in renderfile1.bat to this path as such:
``` txt
@echo off
"\your\path\to\blender\application" --background blank2.blend --python "BlenderAsteroid2.py" 
```
Once this is done, you will need to install the right packages used in this application using the following command: 

``` txt
pip install -r requirements.txt
```
or if this doesn't work, you should try 
``` txt
python -m pip install -r requirements.txt
```
or 
``` txt
python3 -m pip install -r requirements.txt
```

Finally, download all the files in our project in the same folder and run them directly from this folder. 
<br> 
To access this folder in your terminal, you should type (in the terminal from which you are running python)
``` txt
cd \your\path\to\directory\with\all\the\project\code\inside
```
Then you will finally be able to run this project!

### Running the project

Our project runs entirely by just running the ALCS_GUI.py file.
This opens a window like the following: 

![image](https://user-images.githubusercontent.com/90444327/135748240-e270f0b2-a323-4148-9fb4-e649ed668eb5.png)

### Variables and restrictions

There are 4 parameters you can input:
* Camera Position 
  * The position where we place the camera as a 3-dimensional tuple (relative to the origin (0,0,0)) without parenthesis and with a space after each comma. Example input: 10, 0, 0 
* Number of steps
  * The number of steps used as an integer, this will be the number of steps in which the 360 degree rotation will be divided. For instance, if we say the number of steps is 2, we will have images of the asteroid at 0 and 180 degrees. Example input: 360
* Rotational Axis
  * The axis of rotation as a 3-dimensional tuple (relative to the origin (0,0,0)) without parenthesis and with a space after each comma. Example input: 0, 0, 1
* Filename 
  * The filename of the asteroid object we want to get the lightcurve for (which ends in .obj) as a string. Example input: 1996hw1.obj

Before running this code, be sure to save the asteroid object in the same folder as all the code used for this project.
<br>
Also note that the asteroid object will be placed at the origin and thus the camera position and rotational axis are relative to the center of the asteroid.
<br>
Once you have inserted all parameters, you can click Run to generate the lightcurve of your chosen asteroid.
<br>
Clicking the run button will generate the following:
* Images of the asteroids at the different degrees specified by the Number of steps
  * These will be stored in a newly created Image folder (the amount of images inside the folder is the number of steps you input)
* Lightcurve plot
  * Plot of the lightcurve of the asteroid, where points are obtained at the angles specified by the Number of steps
* A dict.txt file 
  * This file is used to pass the inputted variables onto the python script on Blender

After clicking the run button and allowing time for the program to run, the lightcurve will be plotted on the window as such:

![image](https://user-images.githubusercontent.com/90444327/135749124-7cc960b4-68de-4020-9ef8-3f4982628d0b.png)

The remaining two created objects will appear in the folder the project code is located in as such:

![image](https://user-images.githubusercontent.com/90444327/135749221-505622e5-6ff8-455c-bae7-1f6628cc9b20.png)



