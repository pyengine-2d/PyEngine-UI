from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QImage, QPainter

from pyengine_ui.Core.Utils.PyEngineUtils import *

import pygame


class PyEngineWidget(QWidget):
    def __init__(self, parent):
        super(PyEngineWidget, self).__init__()
        self.parent = parent
        self.image = None  # Respect PEP8
        self.data = None  # Respect PEP8

        self.update_screen()

    def update_screen(self):
        window = self.parent.project.objects[0]

        screen = pygame.Surface((window.properties["Largeur"], window.properties["Hauteur"]))
        screen.fill(window.properties["Couleur"])

        entities = pygame.sprite.Group()
        widgets = pygame.sprite.Group()
        world = self.parent.project.get_object(window.properties["Monde Actuel"])

        for i in world.childs:
            if i.type_ == "Entity":
                entities.add(create_entity(i))
            elif i.type_ == "Label":
                widgets.add(create_label(i))
            elif i.type_ == "Image":
                widgets.add(create_image(i))
            elif i.type_ == "Selector":
                selector = create_selector(i)
                widgets.add(selector.bprecedent)
                widgets.add(selector.bprecedent.label)
                widgets.add(selector.label)
                widgets.add(selector.bnext)
                widgets.add(selector.bnext.label)
            elif i.type_ == "ProgressBar":
                widgets.add(create_progress(i))
            elif i.type_ == "MultilineLabel":
                multiline = create_multiline(i)
                for label in multiline.labels:
                    widgets.add(label)
            elif i.type_ == "Entry":
                widgets.add(create_entry(i))
            elif i.type_ == "Console":
                console = create_console(i)
                widgets.add(console)
                widgets.add(console.retour)
            elif i.type_ == "Checkbox":
                check = create_checkbox(i)
                widgets.add(check)
                widgets.add(check.label)
            elif i.type_ == "Button":
                button = create_button(i)
                widgets.add(button)
                widgets.add(button.label)
            elif i.type_ == "AnimatedImage":
                widgets.add(create_anim(i))

        for i in entities:
            i.rect = i.image.get_rect(center=i.pos)

        entities.draw(screen)
        widgets.draw(screen)

        w = screen.get_width()
        h = screen.get_height()

        self.data = screen.get_buffer().raw
        self.image = QImage(self.data, w, h, QImage.Format_RGB32)
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()


