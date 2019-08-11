import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from pyengine_ui.Core.Window import Window


def launch():
    os.putenv("QT_AUTO_SCREEN_SCALE_FACTOR", "1")

    app = QApplication(sys.argv)
    icon = QIcon(os.path.join(os.path.dirname(__file__), 'logo.png'))
    app.setWindowIcon(icon)

    Window()

    app.exec_()


if __name__ == '__main__':
    launch()
