from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QImage, QPainter

import pygame


class PyEngineWidget(QWidget):
    def __init__(self, parent):
        super(PyEngineWidget, self).__init__()
        self.parent = parent

        self.window = self.parent.project.objects[0]
        self.screen = pygame.Surface((self.window.properties["Largeur"], self.window.properties["Hauteur"]))
        self.screen.fill(self.window.properties["Couleur"])

        w = self.screen.get_width()
        h = self.screen.get_height()

        self.data = self.screen.get_buffer().raw
        self.image = QImage(self.data, w, h, QImage.Format_RGB32)

    def update_screen(self):
        self.window = self.parent.project.objects[0]

        self.screen = pygame.Surface((self.window.properties["Largeur"], self.window.properties["Hauteur"]))
        self.screen.fill(self.window.properties["Couleur"])

        w = self.screen.get_width()
        h = self.screen.get_height()

        self.data = self.screen.get_buffer().raw
        self.image = QImage(self.data, w, h, QImage.Format_RGB32)
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()


