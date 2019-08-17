from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

from pyengine_ui.Core.Widgets import ListWidget, Label

import os
import json


class ThemesWindow(QDialog):
    def __init__(self, parent):
        super(ThemesWindow, self).__init__()
        self.parent = parent
        self.setWindowTitle("PyEngine - Themes")
        self.setFixedSize(600, 400)
        self.grid = QGridLayout()

        self.title = Label("Thèmes", 18)
        self.title.setAlignment(Qt.AlignHCenter)
        self.liste = []
        for i in os.listdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes")):
            if "theme.json" in os.listdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i)):
                fichier = open(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i, "theme.json"),
                               "r", encoding="utf-8")
                jsonfile = json.load(fichier)
                jsonfile["folder"] = i
                self.liste.append(jsonfile)
            else:
                print("ERREUR : Le theme du dossier "+i+" n'a pas de json.")
        self.listeW = ListWidget(self.liste, "Themes")
        self.supp = QPushButton("Supprimer")
        self.suppAll = QPushButton("Tout supprimer")

        self.listeW.itemClicked.connect(self.launch)
        self.suppAll.clicked.connect(self.deleteall)
        self.supp.clicked.connect(self.delete)

        self.grid.addWidget(self.title, 1, 1, 1, 2)
        self.grid.addWidget(self.listeW, 2, 1, 1, 2)
        self.grid.addWidget(self.supp, 3, 1)
        self.grid.addWidget(self.suppAll, 3, 2)

        self.setLayout(self.grid)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def launch(self):
        if self.listeW.currentItem():
            for i in self.liste:
                if i["folder"] == self.listeW.currentItem().text(3):
                    self.parent.theme = os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"])
                    self.parent.applytheme()
                    break

    def showupdate(self):
        self.listeW.deleteallitems()
        self.liste = []
        for i in os.listdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes")):
            if "theme.json" in os.listdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i)):
                fichier = open(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i, "theme.json"),
                               "r")
                jsonfile = json.load(fichier)
                jsonfile["folder"] = i
                self.liste.append(jsonfile)
                fichier.close()
            else:
                print("ERREUR : Le theme du dossier "+i+" n'a pas de json.")
        self.listeW.updatelist(self.liste)
        self.show()

    def delete(self):
        if self.listeW.currentItem():
            for i in self.liste:
                if i["folder"] == self.listeW.currentItem().text(3):
                    if self.parent.theme == os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"]):
                        self.parent.theme = ""
                        self.parent.applytheme()
                    contenu = os.listdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"]))
                    for x in contenu:
                        os.remove(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"], x))
                    os.rmdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"]))
        self.showupdate()

    def deleteall(self):
        self.parent.theme = ""
        self.parent.applytheme()
        for i in self.liste:
            contenu = os.listdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"]))
            for x in contenu:
                os.remove(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"], x))
            os.rmdir(os.path.join(os.path.dirname(__file__), "..", "..", "Themes", i["folder"]))
        self.showupdate()
