from PyQt5.QtWidgets import QWidget, QGridLayout, QMessageBox

from pyengine_ui.Core.Widgets import Label
from pyengine_ui.Core.ScriptEditor.EditorWidget import EditorWidget


class Editor(QWidget):
    def __init__(self, parent, obj):
        super(Editor, self).__init__()
        self.parent = parent
        self.obj = obj

        self.grid = QGridLayout()

        label = Label("Script : "+obj.name, 18)
        self.editor = EditorWidget(self)
        self.editor.setPlainText(self.obj.script)

        self.grid.addWidget(label, 0, 0)
        self.grid.addWidget(self.editor, 1, 0)

        self.setLayout(self.grid)
        self.setWindowTitle("PyEngine - Editeur")

    def closeEvent(self, event) -> None:
        if QMessageBox.question(self, "PyEngine - Editeur", "Voulez vous enregistrer le script ?") == QMessageBox.Yes:
            self.obj.script = self.editor.toPlainText()
        event.accept()
