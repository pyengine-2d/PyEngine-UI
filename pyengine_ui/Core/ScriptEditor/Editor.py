from PyQt5.QtWidgets import QWidget, QGridLayout, QTextEdit

from pyengine_ui.Core.Widgets import Label


class Editor(QWidget):
    def __init__(self, parent, obj):
        super(Editor, self).__init__()
        self.parent = parent
        self.obj = obj

        self.grid = QGridLayout()

        label = Label("Script : "+obj.name, 18)
        self.textedit = QTextEdit(obj.script)

        self.grid.addWidget(label, 0, 0)
        self.grid.addWidget(self.textedit, 1, 0)

        self.setLayout(self.grid)
