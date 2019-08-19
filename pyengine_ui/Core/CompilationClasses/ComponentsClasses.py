import os
import shutil


def add_init():
    text = "        try:\n"
    text += "            self.init()\n"
    text += "        except AttributeError:\n"
    text += "            pass\n"
    return text


def control_class(compil, con):
    type_ = str(con.properties["Type de Controle"])
    speed = str(con.properties["Vitesse"])

    text = "from pyengine.Components import ControlComponent\nfrom pyengine import ControlType, Controls, const\n\n\n"
    text += "class " + con.name + "(ControlComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + con.name + ", self).__init__(ControlType." + type_ + ", " + speed + ")\n"
    text += add_init()
    if con.script != "":
        text += "    \n"
        for i in con.script.split("\n"):
            text += "    " + i + "\n"
    return text


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
    text += add_init()
    if pos.script != "":
        text += "    \n"
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
    text += add_init()
    if sprite.script != "":
        text += "    \n"
        for i in sprite.script.split("\n"):
            text += "    " + i + "\n"
    return text


def physics_class(compil, phys):
    agravity = str(phys.properties["Affecté par Gravité"])
    fric = str(phys.properties["Friction"])
    elas = str(phys.properties["Elasticité"])
    mass = str(phys.properties["Masse"])
    solid = str(phys.properties["Solide"])
    rotation = str(phys.properties["Rotation"])

    text = "from pyengine.Components import PhysicsComponent\n\n\n"
    text += "class " + phys.name + "(PhysicsComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + phys.name + ", self).__init__(" + agravity + ", " + fric + ", " + elas + ", " + \
            mass + ", " + solid + ", " + rotation + ")\n"
    text += add_init()
    if phys.script != "":
        text += "    \n"
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
    text += add_init()
    if move.script != "":
        text += "    \n"
        for i in move.script.split("\n"):
            text += "    " + i + "\n"
    return text


def text_class(compil, txt):
    texte = str(txt.properties["Texte"])
    scale = str(txt.properties["Scale"])
    color = txt.properties["Couleur"]
    text = "from pyengine.Components import TextComponent\nfrom pyengine.Utils import Color, Font\n\n\n"
    text += "class " + txt.name + "(TextComponent):\n"
    text += "    def __init__(self):\n"
    text += "        super(" + txt.name + ', self).__init__("' + texte + '", Color(' + str(color[0]) + ", " \
    text += ", scale=" + scale + ")\n"
    text += add_init()
    if txt.script != "":
        text += "    \n"
        for i in txt.script.split("\n"):
            text += "    " + i + "\n"
    return text