import os
import shutil


def add_init():
    text = "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    return text


def world_class(self, world):
    gravity_x = str(world.properties["Gravité X"])
    gravity_y = str(world.properties["Gravité Y"])

    text = "from pyengine import World\n"
    if len(world.childs):
        text += "from pyengine.Systems import EntitySystem\n"
        for i in world.childs:
            text += "from Entities." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + world.name + "(World):\n"
    text += "    def __init__(self, window):\n"
    text += "        super(" + world.name + ", self).__init__(window, [" + gravity_x + ", " + gravity_y + "])\n"
    text += add_init()
    if len(world.childs):
        text += "        self.esys = self.get_system(EntitySystem)\n"
        for i in world.childs:
            text += "        self.esys.add_entity(" + i.name + "())\n"
    if world.script != "":
        text += "    \n"
        for i in world.script.split("\n"):
            text += "    " + i + "\n"
    return text


def window_class(compil, window):
    largeur = str(window.properties["Largeur"])
    hauteur = str(window.properties["Hauteur"])
    color = window.properties["Couleur"]
    titre = str(window.properties["Titre"])
    icon = str(window.properties["Icon"])
    if window.properties["FPS Max"] == 0:
        fps = str(None)
    else:
        fps = str(window.properties["FPS Max"])
    update = str(window.properties["Update /s"])
    debug = str(window.properties["Debug"])

    if icon != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(icon)
        shutil.copyfile(icon, os.path.join(directory, "Images", filename))
        icon = "Images/" + filename

    text = "from pyengine import Window\nfrom pyengine.Utils import Color\n"
    if len(window.childs):
        for i in window.childs:
            text += "from Worlds." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + window.name + "(Window):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + window.name + ", self).__init__(" + largeur + ", " + hauteur + ", Color(" + \
            str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")"
    if titre != "":
        text += ', title="' + titre + '"'
    if icon != "":
        text += ', icon="' + icon + '"'
    text += ", limit_fps=" + fps + ", update_rate=" + update + ", debug=" + debug + ")\n"
    text += add_init()
    if len(window.childs):
        i = None
        for i in window.childs:
            text += "        self." + i.name.lower() + " = " + i.name + "(self)\n"
        text += "        self.world = self." + i.name.lower() + "\n"
    text += "        self.run()\n"
    if window.script != "":
        text += "    \n"
        for i in window.script.split("\n"):
            text += "    " + i + "\n"
    text += "\n\n" + window.name + "()\n"
    return text
