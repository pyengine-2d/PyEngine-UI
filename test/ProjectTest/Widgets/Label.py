from pyengine.Widgets import Label
from pyengine.Utils import Vec2, Color, Font


class Label(Label):
    def __init__(self):
        super(Label, self).__init__(Vec2(525, 525), "Mamadou !", Color(255, 0, 4), Font("arial", 26, True, True, True))
        try:
            self.init()
        except AttributeError:
            pass
