import os
import shutil


def add_init():
    text = "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    return text


def tilemap_class(compil, tilemap):
    pos_x = str(tilemap.properties["Position X"])
    pos_y = str(tilemap.properties["Position Y"])
    file = str(tilemap.properties["Fichier JSON"])
    scale = str(tilemap.properties["Scale"])

    if file != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "JSON"), exist_ok=True)
        filename = os.path.basename(file)
        shutil.copyfile(file, os.path.join(directory, "JSON", filename))
        file = "JSON/" + filename

    text = "from pyengine.Entities import Tilemap\nfrom pyengine.Utils import Vec2\n"
    if len(tilemap.childs):
        for i in tilemap.childs:
            text += "from Components." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + tilemap.name + "(Tilemap):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + tilemap.name + ", self).__init__(Vec2(" + pos_x + ", " + pos_y + "), " + file + \
            ", " + scale + ")\n"
    text += add_init()
    if len(tilemap.childs):
        for i in tilemap.childs:
            text += "        self.add_component(" + i.name + "())\n"
    if tilemap.script != "":
        text += "    \n"
        for i in tilemap.script.split("\n"):
            text += "    " + i + "\n"
    return text


def entity_class(compil, entity):
    text = "from pyengine.Entities import Entity\n"
    if len(entity.childs):
        for i in entity.childs:
            text += "from Components." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + entity.name + "(Entity):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + entity.name + ", self).__init__()\n"
    text += add_init()
    if len(entity.childs):
        for i in entity.childs:
            text += "        self.add_component(" + i.name + "())\n"
    if entity.script != "":
        text += "    \n"
        for i in entity.script.split("\n"):
            text += "    " + i + "\n"
    return text