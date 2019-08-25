from pyengine.Widgets import Image
from pyengine.Utils import Vec2


class Image(Image):
    def __init__(self):
        super(Image, self).__init__(Vec2(700, 100), "Images/idle.png")
        try:
            self.init()
        except AttributeError:
            pass
