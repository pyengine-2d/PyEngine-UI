import os
import shutil


def add_init():
    return "        try:\n", "            self.init()\n", "        except AttributeError:\n", "            pass\n"


def world_class(self, world):
    gravity_x = str(world.properties["Gravité X"])
    gravity_y = str(world.properties["Gravité Y"])

    text = ["from pyengine import World\n"]
    if len(world.childs):
        text.append("from pyengine.Systems import EntitySystem\n")
        text.append("from pyengine.Systems import UISystem\n")
        for i in world.childs:
            if i.type_ in ["Entity", "Tilemap"]:
                text.append("from Entities." + i.name.capitalize() + " import " + i.name + "\n")
            else:
                text.append("from Widgets." + i.name.capitalize() + " import " + i.name  + "\n")
    text += [
        "\n\nclass " + world.name + "(World):\n",
        "    def __init__(self, window):\n",
        "        super(" + world.name + ", self).__init__(window, [" + gravity_x + ", " + gravity_y + "])\n"
    ]
    text += add_init()
    if len(world.childs):
        text.append("        self.esys = self.get_system(EntitySystem)\n")
        text.append("        self.uisys = self.get_system(UISystem)\n")
        for i in world.childs:
            if i.type_ in ["Entity", "Tilemap"]:
                text.append("        self.esys.add_entity(" + i.name + "())\n")
            elif i.type_ == "Console":
                text.append("        self.uisys.add_widget(" + i.name + "(self.window))")
            else:
                text.append("        self.uisys.add_widget(" + i.name + "())\n")
    if world.script != "":
        text.append("    \n")
        for i in world.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


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

    text = ["from pyengine import Window\nfrom pyengine.Utils import Color\n"]
    if len(window.childs):
        for i in window.childs:
            text.append("from Worlds." + i.name.capitalize() + " import " + i.name + "\n")
    text += [
        "\n\nclass " + window.name + "(Window):\n",
        "    def __init__(self):\n",
        "        super(" + window.name + ", self).__init__(" + largeur + ", " + hauteur + ", Color(" + str(color[0]) +
        ", " + str(color[1]) + ", " + str(color[2]) + ")"
    ]
    if titre != "":
        text.append(', title="' + titre + '"')
    if icon != "":
        text.append(', icon="' + icon + '"')
    text.append(", limit_fps=" + fps + ", update_rate=" + update + ", debug=" + debug + ")\n")
    text += add_init()
    if len(window.childs):
        i = None
        for i in window.childs:
            text.append("        self." + i.name.lower() + " = " + i.name + "(self)\n")
        text.append("        self.world = self." + i.name.lower() + "\n")
    text.append("        self.run()\n")
    if window.script != "":
        text.append("    \n")
        for i in window.script.split("\n"):
            text.append("    " + i + "\n")
    text.append("\n\n" + window.name + "()\n")
    return "".join(text)
