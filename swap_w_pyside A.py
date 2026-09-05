import os 
import sys

import bpy
from PySide6 import QtWidgets, QtGui, QtUiTools


# __file__ gives us the current .py file
DIR_PATH  = '/Users/Koxen/Library/CloudStorage/OneDrive-Personal/file stream/Python for Blender/Final App'
IMG_PATH  = DIR_PATH + '/img/scene_swap.jpg'
LOGO_PATH = DIR_PATH + '/img/blender.png'
UI_PATH   = DIR_PATH + "/wk10_swap.ui"

worlds = {
    'World 1':[],
    'World 2':[],
    'World 3':[]
    }

def print_worlds():
    print(f'world 1: {worlds[0]}')
    print(f'world 2: {worlds[1]}')
    print(f'world 3: {worlds[2]}\n')

class ArScene:
    def __init__(self):        
        # LOAD ui
        self.wg_util = QtUiTools.QUiLoader().load(UI_PATH)

        # CONNECT button with function
        self.wg_util.btn_new_world.clicked.connect(self.press_new_world)
        self.wg_util.btn_clear.clicked.connect(self.press_clear)
        self.wg_util.btn_add.clicked.connect(self.press_add)
        self.wg_util.btn_remove.clicked.connect(self.press_remove)
        self.wg_util.btn_hide.clicked.connect(self.press_hide)
        self.wg_util.btn_unhide.clicked.connect(self.press_unhide)

        # ADD pixmap image
        pixmap = QtGui.QPixmap(IMG_PATH)
        self.wg_util.lbl_image.setPixmap(pixmap)  
        self.wg_util.setWindowIcon(QtGui.QIcon(LOGO_PATH))

        # SHOW the UI
        self.wg_util.show()

    #************************************************************
    # PRESS
    def press_new_world(self):
        # ADD new world to the list of worlds
        count = self.wg_util.cbx_worlds.count()
        name = 'World ' + str(count + 1)

        # ADD new world to the list of worlds
        self.wg_util.cbx_worlds.addItem(name)
        print("New world: " + name)

    def press_clear(self):
        # DELETE all items in the combobox
        self.wg_util.cbx_worlds.clear()
        print("All worlds are gone!")

    def press_add(self):
        wrld_select_cbx = self.wg_util.cbx_worlds.currentText()
        active_asset = bpy.context.view_layer.objects.active

        if active_asset.name in wrld_select_cbx:
            print(f'asset {active_asset} already in {wrld_select_cbx}')
        else:
            worlds[wrld_select_cbx].append(active_asset)
          

        '''match wrld_select_cbx:
            case 'World 1':
                if active_asset in world1:
                    print(f'asset {active_asset} already in {wrld_select_cbx}')
                else:
                    world1.append(active_asset)
                print_worlds()
            case 'World 2':
                world2.append(active_asset)
                print_worlds()
            case 'World 3':
                world3.append(active_asset)
                print_worlds()'''
        
        print(f"Selected Asset: {active_asset} added to {wrld_select_cbx} " )
        print_worlds()

    def press_remove(self):
        print("Asset removed!")

    def press_hide(self):
        print("All assets are hidden!")

    def press_unhide(self):
        print("All assets are revealed!")



#*******************************************************************
# START
# OS start
# ONLY needed if also used in the operation system
def create():
    app = QtWidgets.QApplication(sys.argv)
    main_widget = ArScene()
    sys.exit(app.exec_())


# DCC start
def start():
    global main_widget

    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)

    main_widget = ArScene()

start()