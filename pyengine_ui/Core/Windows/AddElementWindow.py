from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLineEdit, QSpacerItem, QListWidget, QMessageBox

from pyengine_ui.Core.Widgets import Label
from pyengine_ui.Core.Utils import types, get_parent_types, Object


class AddElementWindow(QDialog):
    def __init__(self, parent):
        super(AddElementWindow, self).__init__()
        self.parent = parent
        self.setWindowTitle("PyEngine - Element")

        self.grid = QGridLayout()

        ltitle = Label("Elements", 15)
        ltitle.setAlignment(Qt.AlignHCenter)
        lname = Label("Nom", 12)
        lname.setAlignment(Qt.AlignHCenter)
        self.nameInput = QLineEdit()
        ltype = Label("Type", 12)
        ltype.setAlignment(Qt.AlignHCenter)
        self.typelist = QListWidget()
        self.typelist.addItems([i for i in types])
        lparent = Label("Parent", 12)
        lparent.setAlignment(Qt.AlignHCenter)
        self.parentlist = QListWidget()
        self.go = QPushButton("Entrer")
        self.cancel = QPushButton("Annuler")
        spacer = QSpacerItem(20, 25)

        self.go.clicked.connect(self.enter)
        self.cancel.clicked.connect(self.close)
        self.typelist.currentItemChanged.connect(self.item_changed)

        self.grid.addWidget(ltitle, 0, 0, 1, 2)
        self.grid.addItem(spacer, 1, 0)
        self.grid.addWidget(lname, 2, 0, 1, 2)
        self.grid.addWidget(self.nameInput, 3, 0, 1, 2)
        self.grid.addItem(spacer, 4, 0)
        self.grid.addWidget(ltype, 5, 0, 1, 2)
        self.grid.addWidget(self.typelist, 6, 0, 1, 2)
        self.grid.addItem(spacer, 7, 0)
        self.grid.addWidget(lparent, 8, 0, 1, 2)
        self.grid.addWidget(self.parentlist, 9, 0, 1, 2)
        self.grid.addWidget(self.go, 10, 0)
        self.grid.addWidget(self.cancel, 10, 1)

        self.grid.setContentsMargins(10, 10, 10, 10)

        self.setLayout(self.grid)
        self.setFixedSize(400, 500)

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def enter(self):
        if self.nameInput.text() == "":
            QMessageBox.warning(self, "Erreur", "Le nom de l'élément n'a pas été fourni")
        elif self.typelist.currentItem() is None:
            QMessageBox.warning(self, "Erreur", "Le type de l'élément n'a pas été fourni")
        elif self.parentlist.currentItem() is None:
            QMessageBox.warning(self, "Erreur", "Le parent de l'élément n'a pas été fourni")
        else:
            for v in self.parent.project.all_objects():
                if v.name == self.parentlist.currentItem().text():
                    obj = Object(self.nameInput.text(), self.typelist.currentItem().text())
                    obj.parent = v
                    v.childs.append(obj)
                    break
            self.parent.elements.update_items()
            self.close()

    def item_changed(self, current, previous):
        item = current.text()
        self.parentlist.clear()
        self.parentlist.addItems(
            [v.name for v in self.parent.project.all_objects() if v.type_ in get_parent_types(item)]
        )


