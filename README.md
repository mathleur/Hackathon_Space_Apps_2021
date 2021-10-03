# Hackathon_Space_Apps_2021

## How to use this repository

### Before starting
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

Finally, download all the files in our project in the same folder and run them directly from this folder. 
<br> 
To access this folder in your terminal, you should type in 
``` txt
cd \your\path\to\directory\with\all\the\project\code\inside
```
Then you will finally be able to run this project!

### Starting

open the ALCS_GUI.py

There are 4 parameters you can type in which includes
1) Camera Position in 3d- tuples
2) Number of steps
3) Rotational-Axis
4) filename of the 3d model for example as an .obj

![image](https://user-images.githubusercontent.com/90444327/135748240-e270f0b2-a323-4148-9fb4-e649ed668eb5.png)


