from pyengine.Components import PositionComponent
from pyengine.Utils import Vec2


class Position(PositionComponent):
    def __init__(self):
        super(Position, self).__init__(Vec2(200, 100), Vec2(0, 0))
        try:
            self.init()
        except AttributeError:
            pass
