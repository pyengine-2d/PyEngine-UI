import pyengine
from PySide2.QtCore import Qt, QLibraryInfo
from PySide2.QtWidgets import QDialog, QGridLayout, QSpacerItem
import PySide2

import pyengine_ui
from pyengine_ui.Core.Widgets import Label


class InformationsWindow(QDialog):
    def __init__(self, parent):
        super(InformationsWindow, self).__init__()
        self.parent = parent
        self.setWindowTitle("PyEngine - A Propos")
        self.setFixedSize(500, 300)

        self.grid = QGridLayout()

        title = Label("PyEngine", 18)
        title.setAlignment(Qt.AlignHCenter)

        tvpyengine = Label("Version PyEngine : ", 15)
        vpyengine = Label(pyengine.__version__, 15)
        vpyengine.setAlignment(Qt.AlignHCenter)

        tvpyengine_ui = Label("Version PyEngine-UI : ", 15)
        vpyengine_ui = Label(pyengine_ui.__version__, 15)
        vpyengine_ui.setAlignment(Qt.AlignHCenter)

        tvpyqt = Label("Version PySide2 : ", 15)
        vpyqt = Label(PySide2.__version__, 15)
        vpyqt.setAlignment(Qt.AlignHCenter)

        tvqt = Label("Version Qt : ", 15)
        vqt = Label(QLibraryInfo.version().toString(), 15)
        vqt.setAlignment(Qt.AlignHCenter)

        tauthor = Label("Fait par : ", 15)
        author = Label("Nevinia", 15)
        author.setAlignment(Qt.AlignHCenter)

        self.spacerItem = QSpacerItem(20, 25)

        self.grid.addWidget(title, 0, 0, 1, 2)
        self.grid.addWidget(tvpyengine, 1, 0)
        self.grid.addWidget(vpyengine, 1, 1)
        self.grid.addWidget(tvpyengine_ui, 2, 0)
        self.grid.addWidget(vpyengine_ui, 2, 1)
        self.grid.addWidget(tvpyqt, 3, 0)
        self.grid.addWidget(vpyqt, 3, 1)
        self.grid.addWidget(tvqt, 4, 0)
        self.grid.addWidget(vqt, 4, 1)
        self.grid.addItem(self.spacerItem, 5, 0)
        self.grid.addWidget(tauthor, 6, 0)
        self.grid.addWidget(author, 6, 1)

        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 1)

        self.setLayout(self.grid)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
