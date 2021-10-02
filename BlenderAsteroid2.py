import bpy
import math 
import numpy as np
import os

def directory():
    curr_dir = os.getcwd()
    return curr_dir

#import brightness_calc_single_pic
#from .brightness_calc_single_pic import get_luminance

# This will save parameters 1, 2 , 3 to param1, param2 and param3

## The code below is what you should insert inside blender and it will load that file called 'dict.txt'

def load_dict_from_file():
    f = open('dict.txt', 'r')
    data = f.read()
    f.close()
    return eval(data)

load = load_dict_from_file()

print("Program start")

scene = bpy.context.scene
print("Scene Setup")



lightData = bpy.data.lights.new('light', type = 'SUN')
print("Light Data Added")

light = bpy.data.objects.new('light', lightData)
print("Light Object Added")

scene.collection.objects.link(light)
print("Light Added to Scene")



cameraData = bpy.data.cameras.new('camera')
print("Camera Data Added")

camera = bpy.data.objects.new('camera', cameraData)
print("Camera Object Added")


camera.rotation_euler[0] = math.radians(90)
camera.rotation_euler[2] = math.radians(90)
scene.collection.objects.link(camera)
print("Camera Linked to Scene")


#Change locations if needed
camera.location = load["cameraLoc"]
light.rotation_euler[0] = math.radians(60)
#Replace with input
rotationAxis = load["rotationAxis"]

rotationAxisNormInv = 1/np.linalg.norm(rotationAxis)
rotationAxis = np.multiply(rotationAxis, rotationAxisNormInv)

steps = load["steps"]

rotationVector = np.multiply(rotationAxis, (2*math.pi)/steps)

#Camera location
#Steps
#Rotation Axis
#Light location
#File Name & Location


fileLocation = load["fileUpload"]
importedObject = bpy.ops.import_scene.obj(filepath = fileLocation)
objectSelected = bpy.context.selected_objects[0]
print("Asteroid Imported")




for i in range(steps):
    objectSelected.rotation_euler = objectSelected.rotation_euler+ rotationVector
    bpy.data.scenes["Scene"].camera = camera
    scene.render.image_settings.file_format = 'PNG'
    imageFilePath = directory() + '\\Image\\BlenderImage%d.png'
    scene.render.filepath = imageFilePath.replace("%d",str(i))
    bpy.ops.render.render(write_still = 1) 