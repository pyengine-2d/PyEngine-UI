import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLineEdit, QSpacerItem, QFileDialog, QMessageBox

from pyengine_ui.Core.Widgets import Label


class ProjectWindow(QDialog):
    def __init__(self, parent):
        super(ProjectWindow, self).__init__()
        self.parent = parent
        self.parent_close = True
        self.folder = ""
        self.setWindowTitle("PyEngine - Projet")

        self.grid = QGridLayout()

        self.title = Label("PyEngine", 15)
        self.title.setAlignment(Qt.AlignHCenter)
        self.nameLabel = Label("Nom", 12)
        self.nameLabel.setAlignment(Qt.AlignHCenter)
        self.nameInput = QLineEdit()
        self.folderLabel = Label("Dossier", 12)
        self.folderLabel.setAlignment(Qt.AlignHCenter)
        self.folderButton = QPushButton("Selectionner")
        self.go = QPushButton("Entrer")
        self.cancel = QPushButton("Annuler")
        self.spacerItem = QSpacerItem(20, 25)

        self.go.clicked.connect(self.close_window)
        self.cancel.clicked.connect(self.close)
        self.folderButton.clicked.connect(self.get_folder)

        self.grid.addWidget(self.title, 0, 0, 1, 2)
        self.grid.addItem(self.spacerItem, 1, 0)
        self.grid.addWidget(self.nameLabel, 2, 0, 1, 2)
        self.grid.addWidget(self.nameInput, 3, 0, 1, 2)
        self.grid.addItem(self.spacerItem, 4, 0)
        self.grid.addWidget(self.folderLabel, 5, 0, 1, 2)
        self.grid.addWidget(self.folderButton, 6, 0, 1, 2)
        self.grid.addItem(self.spacerItem, 7, 0)
        self.grid.addWidget(self.go, 8, 0)
        self.grid.addWidget(self.cancel, 8, 1)

        self.grid.setContentsMargins(10, 10, 10, 10)

        self.setLayout(self.grid)
        self.setFixedSize(400, 300)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def get_folder(self):
        directory = os.environ.get('HOME', os.environ.get('USERPROFILE', os.path.dirname(__file__)))
        self.folder = QFileDialog.getExistingDirectory(self, "Dossier du projet", directory,
                                                       QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

    def close_window(self):
        if self.nameInput.text() is None or self.nameInput.text() == "" or self.folder is None or self.folder == "":
            QMessageBox.warning(self, "Erreur", "Le nom ou le dossier du projet est incorrect")
        else:
            self.parent_close = False
            self.parent.project_name = self.nameInput.text()
            self.parent.project_folder = self.folder
            self.close()

    def closeEvent(self, event):
        if self.parent_close:
            self.parent.close()
        event.accept()



