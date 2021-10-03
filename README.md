# Hackathon_Space_Apps_2021

## How to use this repository

### Before starting
Install the Blender application under the path "C:\Program Files\Blender Foundation\Blender 2.93\blender.exe"
Or if the Blender application was installed under another path, change the path in renderfile1.bat to this path as such:
``` txt
@echo off
"\your\path\to\blender\application" --background blank2.blend --python "BlenderAsteroid2.py" 
```

### Starting

open the ALCS_GUI.py

There are 4 parameters you can type in which includes
1) Camera Position in 3d- tuples
2) Number of steps
3) Rotational-Axis
4) filename of the 3d model for example as an .obj
