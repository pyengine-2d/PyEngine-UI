from pyengine.Widgets import Selector
from pyengine.Utils import Vec2


class Selector(Selector):
    def __init__(self):
        super(Selector, self).__init__(Vec2(101, 100), ['Michel', 'Alexis'])
        try:
            self.init()
        except AttributeError:
            pass
