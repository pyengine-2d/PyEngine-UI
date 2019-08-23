import webbrowser

from PySide2.QtWidgets import QMainWindow, QGridLayout, QMessageBox, QWidget

from pyengine_ui.Core.ScriptEditor.EditorWidget import EditorWidget


class Editor(QMainWindow):
    def __init__(self, parent, obj):
        super(Editor, self).__init__()
        self.parent = parent
        self.obj = obj

        self.centralWidget = QWidget()
        self.grid = QGridLayout(self.centralWidget)

        self.script = self.menuBar().addMenu("Script")
        self.script.addAction("Sauvegarder", self.save)
        self.script.addAction("Vérifier")

        self.doc = self.menuBar().addAction("Documentation", self.get_doc)

        self.editor = EditorWidget(self)
        self.editor.setPlainText(self.obj.script)

        self.grid.addWidget(self.editor, 0, 0)

        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle("PyEngine - Script - "+self.obj.name)

    def get_doc(self):
        if self.obj.type_ in ["World", "Window"]:
            url = "https://pyengine-doc.readthedocs.io/fr/latest/API/"+self.obj.type_+".html"
        elif self.obj.type_ in ["Entity", "Tilemap"]:
            url = "https://pyengine-doc.readthedocs.io/fr/latest/API/Entities/"+self.obj.type_+".html"
        elif "Component" in self.obj.type_:
            url = "https://pyengine-doc.readthedocs.io/fr/latest/API/Components/"+self.obj.type_+".html"
        else:
            raise TypeError("Unknown documentation for type : "+self.obj.type_)
        webbrowser.open(url)

    def save(self):
        self.obj.script = self.editor.toPlainText()

    def closeEvent(self, event) -> None:
        if self.obj.script != self.editor.toPlainText():
            if QMessageBox.question(self, "PyEngine - Editeur", "Voulez vous enregistrer le script ?") == QMessageBox.Yes:
                self.save()
        event.accept()
