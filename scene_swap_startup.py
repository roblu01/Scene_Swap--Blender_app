
#******************************************************************************
# STARTUP
#******************************************************************************
# Blender runs every .py in its 'startup' folder on launch and calls register().
# WINDOWS: C:\Users\USER\AppData\Roaming\Blender Foundation\Blender\VERSION\scripts
# 'startup' folder goes inside it (create it if it doesn't exist).

# Get Blender script directory
import bpy
print(bpy.utils.script_paths())

import sys

# 'scene.py' has to sit in this folder, next to this file
sys.path.append('/Applications/Blender.app/Contents/Resources/5.2/scripts/startup/scene_swap')

#******************************************************************************
# SETTINGS
#******************************************************************************
# @persistent keeps our handler alive, else Blender drops it after one file.
from bpy.app.handlers import persistent

@persistent
def set_settings(file_path): # parameter needed
    # ONLY for new files. An existing file keeps its own saved settings.
    if bpy.data.filepath:
        return

    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080

    print("STARTUP: settings loaded")


#******************************************************************************
# REGISTER
#******************************************************************************
import scene_swap

def register():
    # our menu, submenu and panel
    scene_swap.register()

    # run set_settings on a new file
    bpy.app.handlers.load_post.append(set_settings)

    print("STARTUP: menu loaded")


def unregister():
    scene_swap.unregister()
    bpy.app.handlers.load_post.remove(set_settings)