from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget

from pyengine_ui.Core.Widgets.PropertiesWidget import PropertiesWidget


class ElementsWidget(QTreeWidget):
    def __init__(self, parent):
        super(ElementsWidget, self).__init__()
        self.parent = parent

        self.setHeaderLabel("Elements du Projet")

        for t, o in self.parent.project.objects.items():
            treeitem = QTreeWidgetItem([t])
            self.setup_childs(treeitem, o)
            self.addTopLevelItem(treeitem)

        self.expandAll()

        self.itemClicked.connect(self.clickedItem)

    def setup_childs(self, widget, obj):
        for t, o in obj.childs.items():
            child = QTreeWidgetItem([t])
            widget.addChild(child)
            self.setup_childs(child, o)

    def get_item(self, text):
        try:
            return self.findItems(text, Qt.MatchExactly)[0]
        except IndexError:
            return None

    def clickedItem(self, item, column):
        liste = [item.text(0)]
        while item.parent() is not None:
            item = item.parent()
            liste.append(item.text(0))
        liste.reverse()
        obj = None
        for i in liste:
            if obj is None:
                obj = self.parent.project.objects[i]
            else:
                obj = obj.childs[i]

        self.parent.properties.deleteLater()
        self.parent.properties = PropertiesWidget(self.parent, obj)
        self.parent.grid.addWidget(self.parent.properties, 0, 2)
