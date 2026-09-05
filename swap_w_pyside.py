import os 
import sys

import bpy
from PySide6 import QtWidgets, QtGui, QtUiTools


# __file__ gives us the current .py file
DIR_PATH  = os.path.dirname(os.path.abspath(__file__))
IMG_PATH  = DIR_PATH + '/img/scene_swap.jpg'
UI_PATH   = DIR_PATH + "/wk10_swap.ui"

worlds = {
    'World 1':[],
    'World 2':[],
    'World 3':[]
    }

def print_worlds():
    for world_name, assets in worlds.items():
        print(f"{world_name}: {assets}")
    print('')

def show_text(self,current_world):
        text =''
        for asset in worlds[current_world]:
            text += f"{asset.name} - {asset.type}\n"
        self.wg_util.textBrowser.setText(text)

class ArScene:
    def __init__(self):        
        # LOAD ui
        self.wg_util = QtUiTools.QUiLoader().load(UI_PATH)

        # CONNECT button with function
        self.wg_util.btn_new_world.clicked.connect(self.press_new_world)
        self.wg_util.btn_delete_world.clicked.connect(self.press_delete_world)
        self.wg_util.btn_add.clicked.connect(self.press_add)
        self.wg_util.btn_remove.clicked.connect(self.press_remove)
        self.wg_util.btn_hide_toggle.clicked.connect(self.press_hide_toggle)
        self.wg_util.btn_hide.clicked.connect(self.press_hide)
        self.wg_util.btn_reveal.clicked.connect(self.press_reveal)

        # ADD pixmap image
        pixmap = QtGui.QPixmap(IMG_PATH)
        self.wg_util.lbl_image.setPixmap(pixmap)  
        self.wg_util.setWindowIcon(QtGui.QIcon(LOGO_PATH))

        # CONNECT COMBOBOX
        self.wg_util.cbx_worlds.currentIndexChanged.connect(self.world_changed)

        # SHOW the UI
        self.wg_util.show()

    #************************************************************
    def world_changed(self):
        wrld_select_cbx = self.wg_util.cbx_worlds.currentText()
        show_text(self,wrld_select_cbx)

    # PRESS Create Worlds
    def press_new_world(self):
        # count of worlds
        count = self.wg_util.cbx_worlds.count()
        # count up for new world
        name = 'World ' + str(count + 1)

        if count > 9:
            print('World Limit reached!')
        else:
            # ADD new world to the UI list of worlds
            self.wg_util.cbx_worlds.addItem(name)
            worlds[name] = []
            print("New world: " + name)
            print_worlds()

    def press_delete_world(self):
        count_w = self.wg_util.cbx_worlds.count()
        if count_w > 3:
            # DELETE last item in the combobox
            self.wg_util.cbx_worlds.removeItem(self.wg_util.cbx_worlds.count() - 1)
            worlds.popitem()
            print_worlds()
            print("Last World was deleted!\n")
        else:
            print('Three worlds must remain')
    
    # PRESS
    def press_add(self):
        wrld_select_cbx = self.wg_util.cbx_worlds.currentText()
        selected_assets = bpy.context.view_layer.objects.selected

        for asset in selected_assets:
            if asset in worlds[wrld_select_cbx]:
                print(f'asset {asset.name} already in {wrld_select_cbx}')
            else:
                worlds[wrld_select_cbx].append(asset)
                print("Asset Added!")
                print_worlds()
                print(f"Selected Asset: {asset.name} added to {wrld_select_cbx}\n" )
                show_text(self, wrld_select_cbx)


    def press_remove(self):
        wrld_select_cbx = self.wg_util.cbx_worlds.currentText()
        selected_assets = bpy.context.view_layer.objects.selected

        for asset in selected_assets:
            if asset not in worlds[wrld_select_cbx]:
                print('nothing to remove')
                print(f'asset {asset.name} NOT in {wrld_select_cbx}')
            else:
                worlds[wrld_select_cbx].remove(asset)
                print_worlds()
                print("Asset removed!\n")
                show_text(self, wrld_select_cbx)
        

    def press_hide_toggle(self):
        wrld_select_cbx = self.wg_util.cbx_worlds.currentText()

        for asset in worlds[wrld_select_cbx]:
            asset.hide_set(not asset.hide_get())
            asset.hide_render = not asset.hide_render

        show_text(self, wrld_select_cbx)
        print(f"{wrld_select_cbx} visibility toggled!")

    def press_hide(self):
        wrld_select_cbx = self.wg_util.cbx_worlds.currentText()

        for asset in worlds[wrld_select_cbx]:
            asset.hide_set(True)
            asset.hide_render = True

        show_text(self, wrld_select_cbx)
        print("All assets are hidden!")

    def press_reveal(self):
        wrld_select_cbx = self.wg_util.cbx_worlds.currentText()
        
        for asset in worlds[wrld_select_cbx]:
            asset.hide_set(False)
            asset.hide_render = False

        show_text(self, wrld_select_cbx)
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