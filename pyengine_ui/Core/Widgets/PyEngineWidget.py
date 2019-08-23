from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QImage, QPainter

import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pos = [0, 0]
        sprite = ""
        image = None
        rect = None


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

        sprites = pygame.sprite.Group()
        world = self.parent.project.get_object(window.properties["Monde Actuel"])

        for i in world.childs:
            if i.type_ == "Entity":
                entity = Entity()
                for j in i.childs:
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
                sprites.add(entity)

        for i in sprites:
            i.rect = i.image.get_rect(center=i.pos)

        sprites.draw(screen)

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


