from pyengine.Widgets import Button
from pyengine.Utils import Vec2


class Button(Button):
    def __init__(self):
        super(Button, self).__init__(Vec2(800, 600), "OUI", size=Vec2(100, 40))
        try:
            self.init()
        except AttributeError:
            pass
