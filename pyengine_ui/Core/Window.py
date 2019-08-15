import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QVBoxLayout, QPushButton

from pyengine_ui.Core.Utils import parsetheme, Project, Object
from pyengine_ui.Core.Widgets import Label, ElementsWidget, PropertiesWidget
from pyengine_ui.Core.Windows import LaunchWindow, InformationsWindow, ProjectWindow, ThemesWindow

from pyengine.Utils import Config

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.project = Project()

        self.config = Config("config.json")
        if not self.config.created:
            self.config.create({"theme": "default"})

        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        self.elements = ElementsWidget(self)
        self.elementadder = QPushButton("Ajouter un élément")
        self.laffichage = Label("Affichage du Projet", 15)

        self.properties = PropertiesWidget(self, Object("Aucun", "None"))

        self.setup_ui()

        self.windows = {
            "launch": LaunchWindow(self),
            "info": InformationsWindow(self),
            "project": ProjectWindow(self),
            "themes": ThemesWindow(self)
        }

        self.windows["launch"].show()

        self.theme = os.path.join(os.path.dirname(__file__), "..", "Themes", self.config.get("theme"))
        self.applytheme()

    def closeEvent(self, event):
        self.config.set("theme", self.theme)
        self.config.save()
        event.accept()

    def setup_project(self):
        os.makedirs(self.project.project_folder+"/"+self.project.project_name, exist_ok=True)
        self.setWindowTitle('PyEngine - '+self.project.project_name)

    def info_project(self):
        print(self.project.project_name)
        print(self.project.project_folder)

    def applytheme(self):
        if self.theme == "" or self.theme == os.path.join(os.path.dirname(__file__), "..", "Themes"):
            self.theme = os.path.join(os.path.dirname(__file__), "..", "Themes", "default")
        with open(os.path.join(self.theme, "main.pss"), 'r') as fichier:
            pss = parsetheme(fichier.read(), self.theme)
            self.setStyleSheet(pss)
            for i in self.windows.values():
                i.setStyleSheet(pss)

    def open_window(self, type_):
        self.windows[type_].update()
        self.windows[type_].setWindowModality(Qt.ApplicationModal)
        self.windows[type_].show()

    def setup_ui(self):
        project = self.menuBar().addMenu("Projet")
        project.addAction("Modifier", lambda: self.open_window("project"))
        project.addAction("Sauvegarder")
        project.addAction("Contruire")
        project.addAction("Lancer")
        project.addAction("Nouveau Projet")

        parameters = self.menuBar().addMenu("Paramètres")
        parameters.addAction("Thèmes", lambda: self.open_window("themes"))
        parameters.addAction("A Propos", lambda: self.open_window("info"))

        layout_left = QVBoxLayout()
        layout_left.addWidget(self.elements)
        layout_left.addWidget(self.elementadder)
        self.grid.addLayout(layout_left, 0, 0)

        self.laffichage.setAlignment(Qt.AlignHCenter)
        self.grid.addWidget(self.laffichage, 0, 1)

        self.grid.addWidget(self.properties, 0, 2)

        self.grid.setColumnStretch(0, 2)
        self.grid.setColumnStretch(1, 3)
        self.grid.setColumnStretch(2, 2)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle('PyEngine')
