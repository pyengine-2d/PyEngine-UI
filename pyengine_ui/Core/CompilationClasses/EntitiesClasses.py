import os
import shutil
import json
import xml.etree.ElementTree as ET


def add_init():
    return "        try:\n", "            self.init()\n", "        except AttributeError:\n", "            pass\n"


def tilemap_class(compil, tilemap):
    pos_x = str(tilemap.properties["Position X"])
    pos_y = str(tilemap.properties["Position Y"])
    file = str(tilemap.properties["Fichier JSON"])
    scale = str(tilemap.properties["Scale"])

    if file != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Tilemaps", tilemap.name), exist_ok=True)
        filename = os.path.basename(file)
        shutil.copyfile(file, os.path.join(directory, "Tilemaps", tilemap.name, filename))
        with open(file, "r") as f:
            data = json.load(f)
        shutil.copyfile(os.path.join(os.path.dirname(file), data["tilesets"][0]["source"]),
                        os.path.join(directory, "Tilemaps", tilemap.name, "Tileset.tsx"))
        tree = ET.parse(os.path.join(directory, "Tilemaps", tilemap.name, "Tileset.tsx"))
        root = tree.getroot()
        for image in root.iter('image'):
            shutil.copyfile(os.path.join(os.path.dirname(file), os.path.dirname(data["tilesets"][0]["source"]),
                                         image.attrib["source"]), os.path.join(directory, "Tilemaps", tilemap.name,
                                                                               image.attrib["source"]))
        data["tilesets"][0]["source"] = "Tileset.tsx"
        with open(os.path.join(directory, "Tilemaps", tilemap.name, filename), "w") as f:
            json.dump(data, f, indent=4)
        file = "Tilemaps/" + tilemap.name + "/" + filename

    text = ["from pyengine.Entities import Tilemap\nfrom pyengine.Utils import Vec2\n"]
    if len(tilemap.childs):
        for i in tilemap.childs:
            text.append("from Components." + i.name.capitalize() + " import " + i.name + "\n")
    text += [
        "\n\nclass " + tilemap.name + "(Tilemap):\n",
        "    def __init__(self):\n",
        "        super(" + tilemap.name + ", self).__init__(Vec2(" + pos_x + ", " + pos_y + '), "' + file + '", ' +
        scale + ")\n"
    ]
    text += add_init()
    if len(tilemap.childs):
        for i in tilemap.childs:
            text.append("        self.add_component(" + i.name + "())\n")
    if tilemap.script != "":
        text.append("    \n")
        for i in tilemap.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def entity_class(compil, entity):
    text = ["from pyengine.Entities import Entity\n"]
    if len(entity.childs):
        for i in entity.childs:
            text.append("from Components." + i.name.capitalize() + " import " + i.name + "\n")
    text += [
        "\n\nclass " + entity.name + "(Entity):\n",
        "    def __init__(self):\n"
        "        super(" + entity.name + ", self).__init__()\n"
    ]
    text += add_init()
    if len(entity.childs):
        for i in entity.childs:
            text.append("        self.add_component(" + i.name + "())\n")
    if entity.script != "":
        text.append("    \n")
        for i in entity.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)