from pyengine.Widgets import AnimatedImage
from pyengine.Utils import Vec2


class Anim(AnimatedImage):
    def __init__(self):
        super(Anim, self).__init__(Vec2(100, 200), ['Images/sprite0.png', 'Images/sprite1.png', 'Images/test.gif'], 20, Vec2(50, 50))
        try:
            self.init()
        except AttributeError:
            pass
