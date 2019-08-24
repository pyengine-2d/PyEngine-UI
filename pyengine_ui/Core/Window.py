import os

import subprocess

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QFileDialog, QMessageBox
from pyengine.Utils import Config, loggers

from pyengine_ui.Core.Compilation import Compilation
from pyengine_ui.Core.ScriptEditor import Editor
from pyengine_ui.Core.Utils import parsetheme, Project, Object
from pyengine_ui.Core.Widgets import ElementsWidget, PropertiesWidget, PyEngineWidget
from pyengine_ui.Core.Windows import LaunchWindow, InformationsWindow, ProjectWindow, ThemesWindow, AddElementWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loggers.create_logger("PyEngineUI", os.path.join("logs", "pyengineui.log"), True)
        self.project = Project()
        self.compil = Compilation(self.project)

        self.config = Config(os.path.join(os.path.dirname(__file__), "..", "config.json"))
        if not self.config.created:
            self.config.create({"theme": "default", "last_name": "", "last_folder": ""})

        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        self.elements = ElementsWidget(self)
        self.elementdeleter = QPushButton("Supprimer")
        self.elementadder = QPushButton("Ajouter")
        self.affichage = PyEngineWidget(self)

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
        self.config.set("last_name", self.project.project_name)
        self.config.set("last_folder", self.project.project_folder)
        self.config.set("theme", self.theme)
        self.config.save()
        if QMessageBox.question(self, "PyEngine - Projet", "Voulez-vous enregistrer le projet actuel?") \
                == QMessageBox.Yes:
            self.action_on_project("save")
        event.accept()

    def setup_project(self):
        directory = os.path.join(self.project.project_folder, self.project.project_name)
        os.makedirs(directory, exist_ok=True)
        self.setWindowTitle('PyEngine - '+self.project.project_name)
        if os.path.exists(os.path.join(directory, "project.json")):
            self.project.load(os.path.join(directory, "project.json"))
            self.elements.update_items()
        self.affichage.update_screen()

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
                for v in [v for v in self.project.all_objects() if v.name == self.elements.currentItem().text(0)]:
                    if v.parent is None:
                        QMessageBox.warning(self, "PyEngine - Erreur", "Vous ne pouvez pas supprimer la fenêtre.")
                    else:
                        if v.name == self.project.objects[0].properties["Monde Actuel"]:
                            self.project.objects[0].properties["Monde Actuel"] = ""
                        v.parent.childs.remove(v)
                self.elements.update_items()
        elif type_ == "compile":
            self.compil.compile()
        elif type_ == "run":
            self.compil.compile()
            os.chdir(os.path.join(self.project.project_folder, self.project.project_name))
            subprocess.run(["python", os.path.join(self.project.project_folder, self.project.project_name, "Main.py")],
                           capture_output=True)

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

        self.grid.addWidget(self.affichage, 0, 1)

        self.grid.addWidget(self.properties, 0, 2)

        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 3)
        self.grid.setColumnStretch(2, 1)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle('PyEngine')
