
import math
import bpy

#vertices=[(1,1,-1),(1,-1,-1),(-1,-1,-1),(-1,1,-1),(1,1,1),(1,-1,1),(-1,-1,1),(-1,1,1)]
#edges=[]
#faces=[(0,1,2,3),(4,5,6,7),(0,4,7,3),(0,1,5,4),(1,2,6,5),(7,6,2,3)]

#new_mesh = bpy.data.meshes.new("new_mesh")
#new_mesh.from_pydata(vertices,edges,faces)
#new_mesh.update()



#new_object = bpy.data.objects.new("new_object",new_mesh)

view_layer = bpy.context.view_layer
#view_layer.active_layer_collection.collection.objects.link(new_object)


file_loc = 'E:\\Users\\John\\OneDrive\\Hackathon\\Bennu.obj'
imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
obj_object = bpy.context.selected_objects[0]
#print('Imported name', imported_object.name)
print('Imported name: ', obj_object.name)



scene = bpy.context.scene

light_data = bpy.data.lights.new('light', type='SUN')
print("Light data added")
light = bpy.data.objects.new('light', light_data)
print("Light object generated")
light.rotation_euler[0] = math.radians(60)
print("Light placed")
scene.collection.objects.link(light)
print("Light added to scene")


 
cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera', cam_data)
bpy.context.collection.objects.link(cam)
cam.location = (1.5,0,0)
cam.rotation_euler[0] = math.radians(90)
cam.rotation_euler[2] = math.radians(90)

bpy.data.scenes["Scene"].camera = cam
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "E:/Users/John/OneDrive/Hackathon/BlenderImage.png"
bpy.ops.render.render(write_still = 1)



#Run from command line (Almost works)
#Open cmd
#Type e:
#Type cd E:\Program Files\Blender Foundation\Blender 2.93
#Type blender.exe -b --python E:\Users\John\OneDrive\Hackathon\BlenderAsteroid.py