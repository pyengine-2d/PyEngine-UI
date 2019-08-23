from pyengine.Widgets import (Label, Button, Entry, Image, AnimatedImage, MultilineLabel, Console, Checkbox,
                              ProgressBar, Selector)
from pyengine.Utils import Vec2, Color, Font

import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pos = [0, 0]
        sprite = ""
        image = None
        rect = None


def create_entity(obj):
    entity = Entity()
    for j in obj.childs:
        if j.type_ == "PositionComponent":
            entity.pos = [j.properties["Position X"], j.properties["Position Y"]]
        elif j.type_ == "SpriteComponent":
            entity.sprite = j.properties["Image"]
            entity.image = pygame.image.load(j.properties["Image"])
            entity.image = pygame.transform.flip(entity.image, j.properties["Flip X"],
                                                 j.properties["Flip Y"])
            sizescaled = (entity.image.get_rect().width * j.properties["Scale"],
                          entity.image.get_rect().height * j.properties["Scale"])
            entity.image = pygame.transform.scale(entity.image, sizescaled)
            entity.image = pygame.transform.rotate(entity.image, j.properties["Rotation"])
    return entity


def create_label(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    texte = obj.properties["Texte"]
    color = obj.properties["Couleur"]
    font = obj.properties["Font"]
    npolice = obj.properties["Nom Police"]
    tpolice = obj.properties["Taille Police"]
    ipolice = obj.properties["Italique"]
    gpolice = obj.properties["Gras"]
    spolice = obj.properties["Souligné"]
    if font is None:
        return Label(Vec2(posx, posy), texte, Color(color[0], color[1], color[2]), Font(npolice, tpolice, gpolice,
                                                                                        ipolice, spolice))
    else:
        return Label(Vec2(posx, posy), texte, Color(color[0], color[1], color[2]),
                     Font(npolice, tpolice, gpolice, ipolice, spolice), Color(font[0], font[1], font[2]))


def create_selector(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    mots = obj.properties["Mots (séparé d'un -)"].split("-")
    return Selector(Vec2(posx, posy), mots)


def create_progress(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    sizex = obj.properties["Taille X"]
    sizey = obj.properties["Taille Y"]
    imf = obj.properties["Image Fond"]
    imb = obj.properties["Image Barre"]

    if imf is None or imb is None:
        return ProgressBar(Vec2(posx, posy), Vec2(sizex, sizey))
    else:
        return ProgressBar(Vec2(posx, posy), Vec2(sizex, sizey), (imf, imb))


def create_multiline(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    texte = obj.properties["Texte"].replace("\\n", "\n")
    color = obj.properties["Couleur"]
    font = obj.properties["Font"]
    npolice = obj.properties["Nom Police"]
    tpolice = obj.properties["Taille Police"]
    ipolice = obj.properties["Italique"]
    gpolice = obj.properties["Gras"]
    spolice = obj.properties["Souligné"]

    if font is None:
        return MultilineLabel(Vec2(posx, posy), texte, Color(color[0], color[1], color[2]),
                              Font(npolice, tpolice, gpolice, ipolice, spolice))
    else:
        return MultilineLabel(Vec2(posx, posy), texte, Color(color[0], color[1], color[2]),
                              Font(npolice, tpolice, gpolice, ipolice, spolice), Color(font[0], font[1], font[2]))


def create_entry(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    wid = obj.properties["Largeur"]
    image = obj.properties["Image"]
    color = obj.properties["Couleur"]
    npolice = obj.properties["Nom Police"]
    tpolice = obj.properties["Taille Police"]
    ipolice = obj.properties["Italique"]
    gpolice = obj.properties["Gras"]
    spolice = obj.properties["Souligné"]

    return Entry(Vec2(posx, posy), wid, image, Color(color[0], color[1], color[2]), Font(npolice, tpolice, gpolice,
                                                                                         ipolice, spolice))


def create_console(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    wid = obj.properties["Largeur"]
    return Console(None, Vec2(posx, posy), wid)


def create_checkbox(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    text = obj.properties["Texte"]
    check = obj.properties["Coché"]
    scale = obj.properties["Scale"]
    return Checkbox(Vec2(posx, posy), text, check, scale)


def create_button(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    sizex = obj.properties["Taille X"]
    sizey = obj.properties["Taille Y"]
    text = obj.properties["Texte"]
    image = obj.properties["Image"]
    return Button(Vec2(posx, posy), text, size=Vec2(sizex, sizey), sprite=image)


def create_anim(obj):
    posx = obj.properties["Position X"]
    posy = obj.properties["Position Y"]
    images = obj.properties["Images"]
    timer = obj.properties["Timer"]
    sizex = obj.properties["Taille X"]
    sizey = obj.properties["Taille Y"]
    if sizex is None or sizey is None:
        return AnimatedImage(Vec2(posx, posy), images, timer)
    else:
        return AnimatedImage(Vec2(posx, posy), images, timer, Vec2(sizex, sizey))
