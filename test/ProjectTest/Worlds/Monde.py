from pyengine import World
from pyengine.Systems import EntitySystem
from pyengine.Systems import UISystem
from Widgets.Label import Label
from Widgets.Selector import Selector
from Widgets.Progress import Progress
from Widgets.Multiline import Multiline
from Widgets.Entry import Entry
from Widgets.Console import Console
from Widgets.Check import Check
from Widgets.Button import Button
from Widgets.Anim import Anim
from Widgets.Image import Image
from Widgets.Entry2 import Entry2
from Entities.Tile import Tile


class Monde(World):
    def __init__(self, window):
        super(Monde, self).__init__(window, [0, -900])
        try:
            self.init()
        except AttributeError:
            pass
        self.esys = self.get_system(EntitySystem)
        self.uisys = self.get_system(UISystem)
        self.uisys.add_widget(Label())
        self.uisys.add_widget(Selector())
        self.uisys.add_widget(Progress())
        self.uisys.add_widget(Multiline())
        self.uisys.add_widget(Entry())
        self.uisys.add_widget(Console(self.window))
        self.uisys.add_widget(Check())
        self.uisys.add_widget(Button())
        self.uisys.add_widget(Anim())
        self.uisys.add_widget(Image())
        self.uisys.add_widget(Entry2())
        self.esys.add_entity(Tile())
