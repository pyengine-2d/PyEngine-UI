from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from PyQt5.QtCore import Qt

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

        self.grid.addWidget(self.title, 0, 0)

        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setCentralWidget(self.centralWidget)
        self.showMaximized()
        self.setWindowTitle('PyEngine')

