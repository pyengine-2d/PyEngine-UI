import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QSpacerItem, QLineEdit, QCheckBox, QSpinBox, QPushButton, \
    QFileDialog, QSizePolicy, QComboBox, QColorDialog
from PyQt5.QtGui import QColor

from pyengine_ui.Core.Utils import get_properties
from pyengine_ui.Core.Widgets import Label
from pyengine_ui.Core.ScriptEditor import Editor


class PropertiesWidget(QWidget):
    def __init__(self, parent, obj):
        super(PropertiesWidget, self).__init__()
        self.obj = obj
        self.parent = parent
        self.grid = QGridLayout()
        self.grid.setSizeConstraint(self.grid.SetMinAndMaxSize)

        title = Label("Propriété : "+self.obj.type_, 16)
        title.setMaximumHeight(80)
        title.setMinimumHeight(80)
        title.setAlignment(Qt.AlignHCenter)
        self.grid.addWidget(title, 0, 0, 1, 2)
        self.grid.setRowStretch(0, 1)

        nb = 1
        for p in get_properties(self.obj.type_):
            label = Label(p[0], 12)
            label.setMaximumHeight(50)
            label.setMinimumHeight(50)
            self.grid.addWidget(label, nb, 0)

            if p[1] == "str":
                widget = QLineEdit()
                if p[0] == "Nom":
                    widget.setText(self.obj.name)
                else:
                    widget.setText(self.obj.properties.get(p[0], ""))
                widget.textChanged.connect(lambda text="", prop=p[0]: self.set_text_for(text, prop))
            elif p[1] == "bool":
                widget = QCheckBox()
                if self.obj.properties.get(p[0], False):
                    widget.setChecked(True)
                widget.stateChanged.connect(lambda state=0, prop=p[0]: self.set_bool_for(state, prop))
            elif p[1] == "int":
                widget = QSpinBox()
                widget.setMaximum(3000)
                widget.setMinimum(-3000)
                widget.setValue(self.obj.properties.get(p[0], 0))
                widget.valueChanged.connect(lambda value=0, prop=p[0]: self.set_int_for(value, prop))
            elif "|" in p[1] and p[1].split("|")[0] == "list":
                widget = QComboBox()
                for i in p[1].split("|")[1].split(", "):
                    widget.addItem(i)
                widget.setCurrentText(self.obj.properties.get(p[0], p[1].split("|")[1].split(", ")[0]))
                widget.currentTextChanged.connect(lambda value="", prop=p[0]: self.set_text_for(value, prop))
            elif p[1] == "color":
                widget = QPushButton("Sélectionner")
                widget.clicked.connect(lambda checked=False, prop=p[0]: self.set_color_for(prop))
            elif p[1] == "colorNone":
                widget = QWidget()
                layout = QGridLayout()
                select = QPushButton("Sélectionner")
                select.clicked.connect(lambda checked=False, prop=p[0]: self.set_color_for(prop))
                delete = QPushButton("Supprimer")
                delete.clicked.connect(lambda checked=False, prop=p[0]: self.set_none_for(prop))
                layout.addWidget(select, 0, 0)
                layout.addWidget(delete, 0, 1)
                widget.setLayout(layout)
            elif p[1] == "file":
                widget = QPushButton("Sélectionner")
                widget.clicked.connect(lambda checked=False, prop=p[0]: self.set_file_for(prop))
            elif p[1] == "files":
                widget = QPushButton("Sélectionner")
                widget.clicked.connect(lambda checked=False, prop=p[0]: self.set_files_for(prop))
            else:
                raise TypeError("Unknown type for properties : "+p[1])
            self.grid.addWidget(widget, nb, 1)
            self.grid.setRowStretch(nb, 1)

            nb += 1

        scripting = QPushButton("Modifier Script")
        scripting.clicked.connect(self.edit_script)
        self.grid.addWidget(scripting, nb, 0, 1, 2)

        end_spacer = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addItem(end_spacer, nb+1, 0)

        for i in range(0, 2):
            self.grid.setColumnStretch(i, 1)

        self.setLayout(self.grid)

    def edit_script(self):
        if self.obj.type_ != "None":
            self.parent.editor = Editor(self.parent, self.obj)
            self.parent.editor.showMaximized()

    def set_text_for(self, text, prop):
        self.obj.set_property(prop, text)
        if prop == "Nom":
            element = self.parent.elements.get_item(self.obj.name)
            if element is not None:
                element.setText(0, text)
                self.obj.name = text

    def set_bool_for(self, state, prop):
        self.obj.set_property(prop, bool(state))

    def set_int_for(self, value, prop):
        self.obj.set_property(prop, value)

    def set_none_for(self, prop):
        self.obj.set_property(prop, None)

    def set_file_for(self, prop):
        directory = os.environ.get('HOME', os.environ.get('USERPROFILE', os.path.dirname(__file__)))
        self.obj.set_property(prop, QFileDialog.getOpenFileName(self, "Fichier : "+prop, directory)[0])

    def set_files_for(self, prop):
        directory = os.environ.get('HOME', os.environ.get('USERPROFILE', os.path.dirname(__file__)))
        self.obj.set_property(prop, QFileDialog.getOpenFileNames(self, "Fichiers : "+prop, directory)[0])

    def set_color_for(self, prop):
        if self.obj.properties[prop] is not None:
            qcolor = QColorDialog.getColor(QColor(*self.obj.properties[prop]))
        else:
            qcolor = QColorDialog.getColor()
        self.obj.set_property(prop, qcolor.getRgb())


