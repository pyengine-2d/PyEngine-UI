import pyengine
from PyQt5.QtCore import Qt, PYQT_VERSION_STR, QT_VERSION_STR
from PyQt5.QtWidgets import QDialog, QGridLayout, QSpacerItem

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
        tvpyengine.setAlignment(Qt.AlignRight)
        vpyengine = Label(pyengine.__version__, 15)
        vpyengine.setAlignment(Qt.AlignHCenter)

        tvpyengine_ui = Label("Version PyEngine-UI : ", 15)
        tvpyengine_ui.setAlignment(Qt.AlignRight)
        vpyengine_ui = Label(pyengine_ui.__version__, 15)
        vpyengine_ui.setAlignment(Qt.AlignHCenter)

        tvpyqt = Label("Version PyQt : ", 15)
        tvpyqt.setAlignment(Qt.AlignRight)
        vpyqt = Label(PYQT_VERSION_STR, 15)
        vpyqt.setAlignment(Qt.AlignHCenter)

        tvqt = Label("Version Qt : ", 15)
        tvqt.setAlignment(Qt.AlignRight)
        vqt = Label(QT_VERSION_STR, 15)
        vqt.setAlignment(Qt.AlignHCenter)

        tauthor = Label("Fait par : ", 15)
        tauthor.setAlignment(Qt.AlignRight)
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

        self.setLayout(self.grid)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
