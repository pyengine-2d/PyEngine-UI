from pyengine.Widgets import MultilineLabel
from pyengine.Utils import Vec2, Color, Font


class Multiline(MultilineLabel):
    def __init__(self):
        super(Multiline, self).__init__(Vec2(500, 300), "Ceci est un test\nnan ?\nMoi je suis d'accord !", Color(70, 169, 255), Font("arial", 20, False, False, False))
        try:
            self.init()
        except AttributeError:
            pass
