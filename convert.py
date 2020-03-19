import bpy
import os
import glob
from mathutils import Vector

FOLDER_ROOT = os.path.dirname(bpy.context.space_data.text.filepath)

def clearScene():
    for obj in bpy.context.scene.objects:
        bpy.ops.object.delete({"selected_objects": [obj]})

def importScene(fpath):
    clearScene()
    ext = os.path.splitext(fpath)[1]
    if ext == '.gltf' or ext == '.glb':
        bpy.ops.import_scene.gltf(filepath=fpath)
        return True
    if ext == '.obj':
        bpy.ops.import_scene.obj(filepath=fpath)
        return True
    return False
    
def exportScene(orig_inpath):
    fname = os.path.basename(os.path.splitext(orig_inpath)[0])
    ofpath = os.path.join(os.path.join(FOLDER_ROOT, 'output'), '%s.glb' % fname)
    bpy.ops.export_scene.gltf(filepath=ofpath)

def centerObjects():
    # Tranlate objects (recenter):
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
            minx = min([v.x for v in bbox_corners])
            miny = min([v.y for v in bbox_corners])
            maxx = max([v.x for v in bbox_corners])
            maxy = max([v.y for v in bbox_corners])
            w = maxx - minx
            h = maxy - miny
            obj.location.x = 0 - (abs(w) * 0.5)
            obj.location.y = 0 - (abs(h) * 0.5)



for input_path in glob.glob(os.path.join(os.path.join(FOLDER_ROOT, 'input'), '*.*')):
    print("Converting %s" % input_path)
    imported = importScene(input_path)
    if imported == False:
        continue
    centerObjects()
    exportScene(input_path)
    
    
centerObjects()

