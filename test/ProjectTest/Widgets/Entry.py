from pyengine.Widgets import Entry
from pyengine.Utils import Vec2, Color, Font


class Entry(Entry):
    def __init__(self):
        super(Entry, self).__init__(Vec2(10, 500), 200, color=Color(255, 255, 255), font=Font("arial", 15, False, False, False))
        try:
            self.init()
        except AttributeError:
            pass
