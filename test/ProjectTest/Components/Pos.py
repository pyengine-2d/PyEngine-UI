from pyengine.Components import PositionComponent
from pyengine.Utils import Vec2


class Pos(PositionComponent):
    def __init__(self):
        super(Pos, self).__init__(Vec2(100, 200), Vec2(0, 0))
        try:
            self.init()
        except AttributeError:
            pass
