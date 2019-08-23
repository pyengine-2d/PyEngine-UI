from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QSize


class LineAreaWidget(QWidget):
    def __init__(self, editor):
        super(LineAreaWidget, self).__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.linearea_width(), 0)

    def paintEvent(self, event):
        self.editor.linearea_paintevent(event)
