import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout

from pyengine_ui.Core.Utils import parsetheme, Project
from pyengine_ui.Core.Widgets import Label
from pyengine_ui.Core.Windows import ProjectWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.project = Project()

        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        lelement = Label("Elements du Projet", 15)
        lelement.setAlignment(Qt.AlignHCenter)
        self.grid.addWidget(lelement, 0, 0)

        laffichage = Label("Affichage du Projet", 15)
        laffichage.setAlignment(Qt.AlignHCenter)
        self.grid.addWidget(laffichage, 0, 1)

        lprop = Label("Propriétés", 15)
        lprop.setAlignment(Qt.AlignHCenter)
        self.grid.addWidget(lprop, 0, 2)
        self.windows = {
            "launch": LaunchWindow(self),
        }

        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle('PyEngine')
        self.windows["launch"].show()


        self.theme = "Themes/default"
        self.applytheme()

    def setup_project(self):
        os.makedirs(self.project.project_folder+"/"+self.project.project_name, exist_ok=True)
        self.setWindowTitle('PyEngine - '+self.project.project_name)

    def info_project(self):
        print(self.project.project_name)
        print(self.project.project_folder)

    def applytheme(self):
        if self.theme == "" or self.theme == os.path.join(os.path.dirname(__file__), "..", "Themes"):
            self.theme = "Themes/default"
        with open(self.theme + "/main.pss", 'r') as fichier:
            pss = parsetheme(fichier.read(), self.theme)
            self.setStyleSheet(pss)
            for i in self.windows.values():
                i.setStyleSheet(pss)
