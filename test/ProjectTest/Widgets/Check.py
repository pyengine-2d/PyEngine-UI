from pyengine.Widgets import Checkbox
from pyengine.Utils import Vec2


class Check(Checkbox):
    def __init__(self):
        super(Check, self).__init__(Vec2(500, 200), "Mamadou", False, 1)
        try:
            self.init()
        except AttributeError:
            pass
