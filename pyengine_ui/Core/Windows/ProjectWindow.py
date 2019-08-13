from PyQt5.QtWidgets import QDialog, QGridLayout, QSpacerItem, QPushButton, QLineEdit, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt

from pyengine_ui.Core.Widgets import Label


class ProjectWindow(QDialog):
    def __init__(self, parent):
        super(ProjectWindow, self).__init__()
        self.parent = parent
        self.foldermodify = ""
        self.setWindowTitle("PyEngine - Projet")
        self.setFixedSize(500, 300)

        self.grid = QGridLayout()

        title = Label("Projet : "+self.parent.project.project_name, 18)
        title.setAlignment(Qt.AlignHCenter)

        lname = Label("Nom : ", 14)
        self.name = QLineEdit()
        self.name.setText(self.parent.project.project_name)
        print(self.parent.project.project_name)
        lfolder = Label("Dossier : ", 14)
        self.folder = QPushButton("Selectionner")
        lauthor = Label("Auteur : ", 14)
        self.author = QLineEdit()
        self.author.setText(self.parent.project.author)
        lversion = Label("Version : ", 14)
        self.version = QLineEdit(self.parent.project.version)

        self.button_layout = QHBoxLayout()
        self.apply = QPushButton("Appliquer")
        self.cancel = QPushButton("Annuler")
        self.button_layout.addWidget(self.apply)
        self.button_layout.addWidget(self.cancel)

        self.spacerItem = QSpacerItem(20, 25)

        self.folder.clicked.connect(self.get_folder)
        self.cancel.clicked.connect(self.close)
        self.apply.clicked.connect(self.save)

        self.grid.addWidget(title, 0, 0, 1, 2)
        self.grid.addWidget(lname, 1, 0)
        self.grid.addWidget(self.name, 1, 1)
        self.grid.addWidget(lfolder, 2, 0)
        self.grid.addWidget(self.folder, 2, 1)
        self.grid.addWidget(lauthor, 3, 0)
        self.grid.addWidget(self.author, 3, 1)
        self.grid.addWidget(lversion, 4, 0)
        self.grid.addWidget(self.version, 4, 1)
        self.grid.addItem(self.spacerItem, 5, 0, 1, 2)
        self.grid.addLayout(self.button_layout, 6, 0, 1, 2)

        self.setLayout(self.grid)

    def get_folder(self):
        directory = self.parent.project.project_folder
        self.foldermodify = QFileDialog.\
            getExistingDirectory(self, "Dossier du projet", directory,
                                 QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

    def save(self):
        if self.name.text() != "":
            self.parent.project.project_name = self.name.text()
            self.parent.setWindowTitle("PyEngine - "+self.name.text())

        if self.author.text() != "":
            self.parent.project.author = self.author.text()

        if self.foldermodify != "":
            self.parent.project.project_folder = self.foldermodify

        if self.version.text() != "":
            self.parent.project.version = self.version.text()

    def update(self):
        super(ProjectWindow, self).update()
        self.name.setText(self.parent.project.project_name)
        self.author.setText(self.parent.project.author)
        self.version.setText(self.parent.project.version)
        self.foldermodify = self.parent.project.project_folder
