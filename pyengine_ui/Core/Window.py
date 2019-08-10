import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton

from pyengine_ui.Core.Utils import parsetheme
from pyengine_ui.Core.Widgets import Label
from pyengine_ui.Core.Windows import ProjectWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.project_folder = None
        self.project_name = None

        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        self.title = Label("PyEngine", 15)
        self.title.setAlignment(Qt.AlignHCenter)
        self.temp = QPushButton("Info Project")

        self.temp.clicked.connect(self.info_project)

        self.grid.addWidget(self.title, 0, 0)
        self.grid.addWidget(self.temp, 1, 0)

        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setCentralWidget(self.centralWidget)
        self.showMaximized()
        self.setWindowTitle('PyEngine')

        self.projectWindow = ProjectWindow(self)
        self.projectWindow.setWindowModality(Qt.ApplicationModal)
        self.projectWindow.show()

        self.theme = "Themes/default"
        self.applytheme()

    def info_project(self):
        print(self.project_name)
        print(self.project_folder)

    def applytheme(self):
        if self.theme == "" or self.theme == os.path.join(os.path.dirname(__file__), "..", "Themes"):
            self.theme = "Themes/default"
        with open(self.theme + "/main.pss", 'r') as fichier:
            pss = parsetheme(fichier.read(), self.theme)
            self.setStyleSheet(pss)
            self.projectWindow.setStyleSheet(pss)
