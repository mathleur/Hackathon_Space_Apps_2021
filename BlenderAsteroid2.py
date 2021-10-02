import bpy
import math 
import numpy as np

#import brightness_calc_single_pic
#from .brightness_calc_single_pic import get_luminance

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
camera.location = (1.5,0,0)
light.rotation_euler[0] = math.radians(60)
#Replace with input
rotationAxis = (0,0,1)

rotationAxisNormInv = 1/np.linalg.norm(rotationAxis)
rotationAxis = np.multiply(rotationAxis, rotationAxisNormInv)

steps = 360

rotationVector = np.multiply(rotationAxis, (2*math.pi)/steps)

#Camera location
#Steps
#Rotation Axis
#Light location
#File Name & Location


fileLocation = 'E:\\Users\\John\\OneDrive\\Hackathon\\GithubFiles\\Space-Apps-Hackathon\\Asteroid.obj'
importedObject = bpy.ops.import_scene.obj(filepath = fileLocation)
objectSelected = bpy.context.selected_objects[0]
print("Asteroid Imported")




for i in range(steps):
    objectSelected.rotation_euler = objectSelected.rotation_euler+ rotationVector
    bpy.data.scenes["Scene"].camera = camera
    scene.render.image_settings.file_format = 'PNG'
    imageFilePath = "E:\\Users\\John\\OneDrive\\Hackathon\\GithubFiles\\Space-Apps-Hackathon\\BlenderImage%d.png"
    scene.render.filepath = imageFilePath.replace("%d",str(i))
    bpy.ops.render.render(write_still = 1) 