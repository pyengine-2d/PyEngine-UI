import os
import shutil


def position_class(compil, pos):
    pos_x = str(pos.properties["Position X"])
    pos_y = str(pos.properties["Position Y"])
    off_x = str(pos.properties["Offset X"])
    off_y = str(pos.properties["Offset Y"])

    text = "from pyengine.Components import PositionComponent\nfrom pyengine.Utils import Vec2\n\n\n"
    text += "class " + pos.name + "(PositionComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + pos.name + ", self).__init__(Vec2(" + pos_x + ", " + pos_y + "), Vec2(" + off_x + \
            ", " + off_y + "))\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if pos.script != "":
        for i in pos.script.split("\n"):
            text += "    " + i + "\n"
    return text


def sprite_class(compil, sprite):
    image = str(sprite.properties["Image"])
    scale = str(sprite.properties["Scale"])
    rot = str(sprite.properties["Rotation"])
    flipx = str(sprite.properties["Flip X"])
    flipy = str(sprite.properties["Flip Y"])

    if image != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(image)
        shutil.copyfile(image, os.path.join(directory, "Images", filename))
        image = "Images/" + filename

    text = "from pyengine.Components import SpriteComponent\n\n\n"
    text += "class " + sprite.name + "(SpriteComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + sprite.name + ', self).__init__("' + image + '", ' + scale + ", " + rot + ", " + \
            flipx + ", " + flipy + ")\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if sprite.script != "":
        for i in sprite.script.split("\n"):
            text += "    " + i + "\n"
    return text


def physics_class(compil, phys):
    agravity = str(phys.properties["Affecté par Gravité"])
    fric = str(phys.properties["Friction"])
    elas = str(phys.properties["Elasticité"])
    mass = str(phys.properties["Masse"])
    solid = str(phys.properties["Solide"])

    text = "from pyengine.Components import PhysicsComponent\n\n\n"
    text += "class " + phys.name + "(PhysicsComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + phys.name + ", self).__init__(" + agravity + ", " + fric + ", " + elas + ", " + \
            mass + ", " + solid + ")\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if phys.script != "":
        for i in phys.script.split("\n"):
            text += "    " + i + "\n"
    return text


def move_class(compil, move):
    dirx = str(move.properties["Direction X"])
    diry = str(move.properties["Direction Y"])

    text = "from pyengine.Components import MoveComponent\nfrom pyengine.Utils import Vec2\n\n\n"
    text += "class " + move.name + "(MoveComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + move.name + ", self).__init__(Vec2(" + dirx + ", " + diry + "))\n"
    for i in move.script.split("\n"):
        text += "    " + i + "\n"
    return text


def text_class(compil, txt):
    texte = str(txt.properties["Texte"])
    scale = str(txt.properties["Scale"])
    color = txt.properties["Couleur"]

    text = "from pyengine.Components import TextComponent\nfrom pyengine.Utils import Color\n\n\n"
    text += "class " + txt.name + "(TextComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + txt.name + ', self).__init__("' + texte + '", Color(' + str(color[0]) + ", " \
            + str(color[1]) + ", " + str(color[2]) + "), scale=" + scale + ")\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if txt.script != "":
        for i in txt.script.split("\n"):
            text += "    " + i + "\n"
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
    if len(tilemap.childs.values()):
        for i in tilemap.childs.values():
            text += "from Components." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + tilemap.name + "(Tilemap):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + tilemap.name + ", self).__init__(Vec2(" + pos_x + ", " + pos_y + "), " + file + \
            ", " + scale + ")\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if len(tilemap.childs.values()):
        for i in tilemap.childs.values():
            text += "        self.add_component(" + i.name + "())\n"
    if tilemap.script != "":
        for i in tilemap.script.split("\n"):
            text += "    " + i + "\n"
    return text


def entity_class(compil, entity):
    text = "from pyengine.Entities import Entity\n"
    if len(entity.childs.values()):
        for i in entity.childs.values():
            text += "from Components." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + entity.name + "(Entity):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + entity.name + ", self).__init__()\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if len(entity.childs.values()):
        for i in entity.childs.values():
            text += "        self.add_component(" + i.name + "())\n"
    if entity.script != "":
        for i in entity.script.split("\n"):
            text += "    " + i + "\n"
    return text


def world_class(self, world):
    gravity_x = str(world.properties["Gravité X"])
    gravity_y = str(world.properties["Gravité Y"])

    text = "from pyengine import World\n"
    if len(world.childs.values()):
        text += "from pyengine.Systems import EntitySystem\n"
        for i in world.childs.values():
            text += "from Entities." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + world.name + "(World):\n"
    text += "    def __init__(self, window):\n"
    text += "        super(" + world.name + ", self).__init__(window, [" + gravity_x + ", " + gravity_y + "])\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if len(world.childs.values()):
        text += "        self.esys = self.get_system(EntitySystem)\n"
        for i in world.childs.values():
            text += "        self.esys.add_entity(" + i.name + "())\n"
    if world.script != "":
        for i in world.script.split("\n"):
            text += "    " + i + "\n"
    return text


def window_class(compil, window):
    largeur = str(window.properties["Largeur"])
    hauteur = str(window.properties["Hauteur"])
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

    text = "from pyengine import Window\n"
    if len(window.childs.values()):
        for i in window.childs.values():
            text += "from Worlds." + i.name.capitalize() + " import " + i.name + "\n"
    text += "\n\nclass " + window.name + "(Window):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + window.name + ", self).__init__(" + largeur + ", " + hauteur
    if titre != "":
        text += ', title="' + titre + '"'
    if icon != "":
        text += ', icon="' + icon + '"'
    text += ", limit_fps=" + fps + ", update_rate=" + update + ", debug=" + debug + ")\n"
    text += "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    if len(window.childs.values()):
        i = None
        for i in window.childs.values():
            text += "        self." + i.name.lower() + " = " + i.name + "(self)\n"
        text += "        self.world = self." + i.name.lower() + "\n"
    text += "        self.run()\n"
    if window.script != "":
        for i in window.script.split("\n"):
            text += "    " + i + "\n"
    text += "\n\n" + window.name + "()\n"
    return text
