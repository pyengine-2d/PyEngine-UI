from pyengine.Widgets import Selector
from pyengine.Utils import Vec2


class Select(Selector):
    def __init__(self):
        super(Select, self).__init__(Vec2(200, 300), ['Exemple1', 'Exemple2'])
        try:
            self.init()
        except AttributeError:
            pass
