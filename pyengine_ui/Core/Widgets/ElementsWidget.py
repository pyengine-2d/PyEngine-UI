from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTreeWidgetItem, QTreeWidget, QAbstractItemView, QMessageBox

from pyengine_ui.Core.Widgets.PropertiesWidget import PropertiesWidget


class ElementsWidget(QTreeWidget):
    def __init__(self, parent):
        super(ElementsWidget, self).__init__()
        self.parent = parent
        self.dragged = None

        self.setHeaderLabel("Elements du Projet")
        self.setDragEnabled(True)
        self.viewport().setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        self.update_items()

        self.itemClicked.connect(self.clickedItem)

    def update_items(self):
        self.clear()

        for o in self.parent.project.objects:
            treeitem = QTreeWidgetItem([o.name])
            self.setup_childs(treeitem, o)
            self.addTopLevelItem(treeitem)

        self.expandAll()

    def setup_childs(self, widget, obj):
        for o in obj.childs:
            child = QTreeWidgetItem([o.name])
            widget.addChild(child)
            self.setup_childs(child, o)

    def get_item(self, text):
        try:
            return self.findItems(text, Qt.MatchExactly | Qt.MatchRecursive)[0]
        except IndexError:
            return None

    def dropEvent(self, event):
        if not self.dragged.parent():
            QMessageBox.warning(self, "PyEngine - Erreur", "Can't move Window")
            return

        super(ElementsWidget, self).dropEvent(event)

        self.parent.project.update_objects(self.topLevelItem(0))

    def dragEnterEvent(self, e):
        self.dragged = self.currentItem()
        super(ElementsWidget, self).dragEnterEvent(e)

    def clickedItem(self, item, column):
        liste = [item.text(0)]
        while item.parent() is not None:
            item = item.parent()
            liste.append(item.text(0))
        liste.reverse()
        obj = None
        for i in liste:
            if obj is None:
                obj = [o for o in self.parent.project.objects if o.name == i][0]
            else:
                obj = [o for o in obj.childs if o.name == i][0]

        self.parent.properties.deleteLater()
        self.parent.properties = PropertiesWidget(self.parent, obj)
        self.parent.grid.addWidget(self.parent.properties, 0, 2)
