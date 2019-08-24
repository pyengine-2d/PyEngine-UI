from pyengine.Widgets import Console
from pyengine.Utils import Vec2


class Console(Console):
    def __init__(self, window):
        super(Console, self).__init__(window, Vec2(200, 700), 500)
        try:
            self.init()
        except AttributeError:
            pass
