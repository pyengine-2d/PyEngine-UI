from pyengine.Widgets import Entry
from pyengine.Utils import Vec2, Color, Font


class Entry2(Entry):
    def __init__(self):
        super(Entry2, self).__init__(Vec2(0, 0), 200, color=Color(255, 255, 255), font=Font("arial", 15, False, False, False))
        try:
            self.init()
        except AttributeError:
            pass
