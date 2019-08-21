import os
import shutil


def add_init():
    return "        try:\n", "            self.init()\n", "        except AttributeError:\n", "            pass\n"


def selector_class(compil, sel):
    posx = str(sel.properties["Position X"])
    posy = str(sel.properties["Position Y"])
    mots = str(str(sel.properties["Mots (séparé d'un -)"]).split("-"))

    text = [
        "from pyengine.Widgets import Selector\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + sel.name + "(Selector):\n",
        "    def __init__(self):\n",
        "        super(" + sel.name + ", self).__init__(Vec2(" + posx + ", " + posy + "), " + mots + ")\n"
    ]
    text += add_init()
    if sel.script != "":
        text.append("    \n")
        for i in sel.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def progress_class(compil, prog):
    posx = str(prog.properties["Position X"])
    posy = str(prog.properties["Position Y"])
    sizex = str(prog.properties["Taille X"])
    sizey = str(prog.properties["Taille Y"])
    imf = str(prog.properties["Image Fond"])
    imb = str(prog.properties["Image Barre"])

    if imf is not None and imf != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(imf)
        shutil.copyfile(imf, os.path.join(directory, "Images", filename))
        imf = "Images/" + filename

    if imb is not None and imb != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(imb)
        shutil.copyfile(imb, os.path.join(directory, "Images", filename))
        imb = "Images/" + filename

    text = [
        "from pyengine.Widgets import ProgressBar\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + prog.name + "(ProgressBar):\n",
        "    def __init__(self):\n",
        "        super(" + prog.name + ", self).__init__(Vec2(" + posx + ", " + posy + "), Vec2(" + sizex + ", " +
        sizey + ")"
    ]
    if imf is not None and imf != "" and imb is not None and imb != "":
        text.append(", (" + imb + ", " + imf + ")")
    text.append(")\n")
    text += add_init()
    if prog.script != "":
        text.append("    \n")
        for i in prog.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def multiline_class(compil, mll):
    posx = str(mll.properties["Position X"])
    posy = str(mll.properties["Position Y"])
    texte = str(mll.properties["Texte"])
    color = mll.properties["Couleur"]
    font = mll.properties["Font"]
    npolice = str(mll.properties["Nom Police"])
    tpolice = str(mll.properties["Taille Police"])
    ipolice = str(mll.properties["Italique"])
    gpolice = str(mll.properties["Gras"])
    spolice = str(mll.properties["Souligné"])

    text = [
        "from pyengine.Widgets import MultilineLabel\nfrom pyengine.Utils import Vec2, Color\n\n\n",
        "class " + mll.name + "(MutlilineLabel):\n",
        "    def __init__(self):\n",
        "        super(" + mll.name + ", self).__init__(Vec2(" + posx + ", " + posy + '), "' + texte +
        '", Color(' + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + '), Font("' + npolice +
        '", ' + tpolice + ", " + ipolice + ", " + gpolice + ", " + spolice
    ]
    if font is not None:
        text.append(", Color(" + str(font[0]) + ", " + str(font[1]) + ", " + str(font[2]) + ")")
    text.append(")\n")
    text += add_init()
    if mll.script != "":
        text.append("    \n")
        for i in mll.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def label_class(compil, la):
    posx = str(la.properties["Position X"])
    posy = str(la.properties["Position Y"])
    texte = str(la.properties["Texte"])
    color = la.properties["Couleur"]
    font = la.properties["Font"]
    npolice = str(la.properties["Nom Police"])
    tpolice = str(la.properties["Taille Police"])
    ipolice = str(la.properties["Italique"])
    gpolice = str(la.properties["Gras"])
    spolice = str(la.properties["Souligné"])

    text = [
        "from pyengine.Widgets import Label\nfrom pyengine.Utils import Vec2, Color\n\n\n",
        "class " + la.name + "(Label):\n",
        "    def __init__(self):\n",
        "        super(" + la.name + ", self).__init__(Vec2(" + posx + ", " + posy + '), "' + texte +
        '", Color(' + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + '), Font("' + npolice +
        '", ' + tpolice + ", " + ipolice + ", " + gpolice + ", " + spolice
    ]
    if font is not None:
        text.append(", Color(" + str(font[0]) + ", " + str(font[1]) + ", " + str(font[2]) + ")")
    text.append(")\n")
    text += add_init()
    if la.script != "":
        text.append("    \n")
        for i in la.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def image_class(compil, im):
    image = str(im.properties["Image"])
    posx = str(im.properties["Position X"])
    posy = str(im.properties["Position Y"])
    sizex = str(im.properties["Taille X"])
    sizey = str(im.properties["Taille Y"])

    if image != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(image)
        shutil.copyfile(image, os.path.join(directory, "Images", filename))
        image = "Images/" + filename

    text = [
        "from pyengine.Widgets import Image\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + im.name + "(Image):\n",
        "    def __init__(self):\n",
        "        super(" + im.name + ", self).__init__(Vec2(" + posx + ", " + posy + '), "' + image
    ]
    if sizex != 0 and sizey != 0:
        text.append(", Vec2(" + sizex + ", " + sizey + ")")
    text.append(")\n")
    text += add_init()
    if im.script != "":
        text.append("    \n")
        for i in im.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def entry_class(compil, ent):
    posx = str(ent.properties["Position X"])
    posy = str(ent.properties["Position Y"])
    wid = str(ent.properties["Largeur"])
    image = str(ent.properties["Image"])
    color = ent.properties["Couleur"]
    npolice = str(ent.properties["Nom Police"])
    tpolice = str(ent.properties["Taille Police"])
    ipolice = str(ent.properties["Italique"])
    gpolice = str(ent.properties["Gras"])
    spolice = str(ent.properties["Souligné"])

    if image is not None and image != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(image)
        shutil.copyfile(image, os.path.join(directory, "Images", filename))
        image = "Images/" + filename

    text = [
        "from pyengine.Widgets import Entry\nfrom pyengine.Utils import Vec2, Color\n\n\n",
        "class " + ent.name + "(Entry):\n",
        "    def __init__(self):\n",
        "        super(" + ent.name + ", self).__init__(Vec2(" + posx + ", " + posy + "), " + wid
    ]
    if image is not None and image != "":
        text.append(', "' + image + '"')
    text += [
        ", color=Color(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color(2)) + '), font=Font("' + npolice +
        '", ' + tpolice + ", " + ipolice + ", " + gpolice + ", " + spolice + ")\n"
    ]
    text += add_init()
    if ent.script != "":
        text.append("    \n")
        for i in ent.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def console_class(compil, con):
    posx = str(con.properties["Position X"])
    posy = str(con.properties["Position Y"])
    wid = str(con.properties["Largeur"])

    text = [
        "from pyengine.Widgets import Console\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + con.name + "(Console):\n",
        "    def __init__(self, window):\n",
        "        super(" + con.name + ", self).__init__(window, Vec2(" + posx + ", " + posy + "), " + wid + ")\n"
    ]
    text += add_init()
    if con.script != "":
        text.append("    \n")
        for i in con.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def check_class(compil, che):
    posx = str(che.properties["Position X"])
    posy = str(che.properties["Position Y"])
    text = str(che.properties["Texte"])
    check = str(che.properties["Coché"])
    scale = str(che.properties["Scale"])

    text = [
        "from pyengine.Widgets import Checkbox\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + che.name + "(Checkbox):\n",
        "    def __init__(self):\n",
        "        super(" + che.name + ", self).__init__(Vec2(" + posx + ", " + posy + "), " + text+ ", " + check + ", "
        + scale + ")\n"
    ]
    text += add_init()
    if che.script != "":
        text.append("    \n")
        for i in che.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def button_class(compil, but):
    posx = str(but.properties["Position X"])
    posy = str(but.properties["Position Y"])
    sizex = str(but.properties["Taille X"])
    sizey = str(but.properties["Taille Y"])
    comm = str(but.properties["Commande"])
    text = str(but.properties["Texte"])
    image = but.properties["Image"]

    if image is not None and image != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(image)
        shutil.copyfile(image, os.path.join(directory, "Images", filename))
        image = "Images/" + filename

    text = [
        "from pyengine.Widgets import Button\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + but.name + "(Buttton):\n",
        "    def __init__(self):\n",
        "        super(" + but.name + ", self).__init__(Vec2(" + posx + ", " + posy + "), " + text + ", size=Vec2(" +
        sizex + ", " + sizey + ")"
    ]
    if image is not None and image != "":
        text.append(', sprite="' + image + "'")
    text.append(")\n")
    text += add_init()
    if comm != "":
        text.append("        self.command = self." + comm + "\n")
    if but.script != "":
        text.append("    \n")
        for i in but.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def animated_class(compil, anim):
    posx = str(anim.properties["Position X"])
    posy = str(anim.properties["Position Y"])
    images = anim.properties["Images"]
    timer = str(anim.properties["Timer"])
    sizex = str(anim.properties["Taille X"])
    sizey = str(anim.properties["Taille Y"])
    sprites = []

    if images != [] and images != "":
        for i in images:
            directory = os.path.join(compil.project.project_folder, compil.project.project_name)
            os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
            filename = os.path.basename(i)
            shutil.copyfile(i, os.path.join(directory, "Images", filename))
            sprites.append("Images/" + filename)

    text = [
        "from pyengine.Widgets import AnimatedImage\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + anim.name + "(AnimatedImage):\n",
        "    def __init__(self):\n",
        "        super(" + anim.name + ", self).__init__(Vec2(" + posx + ", " + posy + "), " + str(sprites) + ", " +
        timer
    ]
    if sizex != 0 and sizey != 0:
        text.append(", Vec2(" + sizex + ", " + sizey + ")")
    text.append(")\n")
    text += add_init()
    if anim.script != "":
        text.append("    \n")
        for i in anim.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)

