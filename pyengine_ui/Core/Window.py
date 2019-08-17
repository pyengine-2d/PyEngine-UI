import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QFileDialog, QMessageBox

from pyengine_ui.Core.Utils import parsetheme, Project, Object
from pyengine_ui.Core.Widgets import Label, ElementsWidget, PropertiesWidget
from pyengine_ui.Core.Windows import LaunchWindow, InformationsWindow, ProjectWindow, ThemesWindow, AddElementWindow
from pyengine_ui.Core.Compilation import Compilation
from pyengine_ui.Core.ScriptEditor import Editor

from pyengine.Utils import Config


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.project = Project()
        self.compil = Compilation(self.project)

        self.config = Config("config.json")
        if not self.config.created:
            self.config.create({"theme": "default"})

        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        self.elements = ElementsWidget(self)
        self.elementdeleter = QPushButton("Supprimer")
        self.elementadder = QPushButton("Ajouter")
        self.laffichage = Label("Affichage du Projet", 15)

        self.properties = PropertiesWidget(self, Object("Aucun", "None"))

        self.setup_ui()

        self.windows = {
            "launch": LaunchWindow(self),
            "info": InformationsWindow(self),
            "project": ProjectWindow(self),
            "themes": ThemesWindow(self),
            "add": AddElementWindow(self)
        }

        self.editor = None

        self.theme = os.path.join(os.path.dirname(__file__), "..", "Themes", self.config.get("theme"))
        self.applytheme()

        self.editor = Editor(self, Object("Aucun", "None"))

        self.windows["launch"].show()

    def closeEvent(self, event):
        self.config.set("theme", self.theme)
        self.config.save()
        if QMessageBox.question(self, "PyEngine - Projet", "Voulez-vous enregistrer le projet actuel?"):
            self.action_on_project("save")
        event.accept()

    def setup_project(self):
        directory = os.path.join(self.project.project_folder, self.project.project_name)
        os.makedirs(directory, exist_ok=True)
        self.setWindowTitle('PyEngine - '+self.project.project_name)
        if os.path.exists(os.path.join(directory, "project.json")):
            self.project.load(os.path.join(directory, "project.json"))
            self.elements.update_items()

    def applytheme(self):
        if self.theme == "" or self.theme == os.path.join(os.path.dirname(__file__), "..", "Themes"):
            self.theme = os.path.join(os.path.dirname(__file__), "..", "Themes", "default")
        with open(os.path.join(self.theme, "main.pss"), 'r') as fichier:
            pss = parsetheme(fichier.read(), self.theme)
            self.setStyleSheet(pss)
            for i in self.windows.values():
                i.setStyleSheet(pss)
            if self.editor is not None:
                self.editor.editor.highlighter.update_styles()
                self.editor.editor.highlighter.update_rules()

    def open_window(self, type_):
        self.windows[type_].update()
        self.windows[type_].setWindowModality(Qt.ApplicationModal)
        self.windows[type_].show()

    def action_on_project(self, type_):
        if type_ == "save":
            self.project.save()
            self.elements.update_items()
        elif type_ == "load":
            if QMessageBox.question(self, "PyEngine - Projet",
                                    "Voulez-vous enregistrer le projet actuel?") == QMessageBox.Yes:
                self.action_on_project("save")
            file = QFileDialog.getOpenFileName(self, "Fichier du projet", self.project.project_folder,
                                               "Fichier Projet (*.json)")
            if file != "":
                self.project.load(file[0])
                self.setWindowTitle("PyEngine - "+self.project.project_name)
        elif type_ == "new":
            self.close()
            self.windows["launch"].show()
        elif type_ == "deleteE":
            if self.elements.currentItem() is not None:
                obj = [v for k, v in self.project.all_objects().items() if k == self.elements.currentItem().text(0)][0]
                del obj.parent.childs[obj.name]
                self.elements.update_items()
        elif type_ == "compile":
            self.compil.compile()
        elif type_ == "run":
            self.compil.compile()
            os.chdir(os.path.join(self.project.project_folder, self.project.project_name))
            os.system("python "+os.path.join(self.project.project_folder, self.project.project_name, "Main.py"))

    def setup_ui(self):
        project = self.menuBar().addMenu("Projet")
        project.addAction("Modifier", lambda: self.open_window("project"))
        project.addAction("Sauvegarder", lambda: self.action_on_project("save"))
        project.addAction("Charger", lambda: self.action_on_project("load"))
        project.addAction("Compiler", lambda: self.action_on_project("compile"))
        project.addAction("Lancer", lambda: self.action_on_project("run"))
        project.addAction("Nouveau Projet", lambda: self.action_on_project("new"))

        parameters = self.menuBar().addMenu("Paramètres")
        parameters.addAction("Thèmes", lambda: self.open_window("themes"))
        parameters.addAction("A Propos", lambda: self.open_window("info"))

        self.elementadder.clicked.connect(lambda: self.open_window("add"))
        self.elementdeleter.clicked.connect(lambda: self.action_on_project("deleteE"))

        layout_left = QGridLayout()
        layout_left.addWidget(self.elements, 0, 0, 1, 2)
        layout_left.addWidget(self.elementdeleter, 1, 0)
        layout_left.addWidget(self.elementadder, 1, 1)
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
