from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget

from pyengine_ui.Core.Widgets.PropertiesWidget import PropertiesWidget


class ElementsWidget(QTreeWidget):
    def __init__(self, parent):
        super(ElementsWidget, self).__init__()
        self.parent = parent

        self.setHeaderLabel("Elements du Projet")

        self.window = QTreeWidgetItem(["Window"])
        self.addTopLevelItem(self.window)
        self.expandAll()

        self.itemClicked.connect(self.clickedItem)

    def clickedItem(self, item, column):
        self.parent.properties.deleteLater()
        self.parent.properties = PropertiesWidget(self.parent.project.objects[item.text(0)])
        self.parent.grid.addWidget(self.parent.properties, 0, 2)
