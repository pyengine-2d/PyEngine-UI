from pyengine import World
from pyengine.Systems import EntitySystem
from pyengine.Systems import UISystem
from Entities.E import E
from Widgets.Select import Select


class Monde(World):
    def __init__(self, window):
        super(Monde, self).__init__(window, [0, -900])
        try:
            self.init()
        except AttributeError:
            pass
        self.esys = self.get_system(EntitySystem)
        self.uisys = self.get_system(UISystem)
        self.esys.add_entity(E())
        self.uisys.add_widget(Select())
