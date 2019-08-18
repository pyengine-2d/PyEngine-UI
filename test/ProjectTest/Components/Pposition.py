from pyengine.Components import PositionComponent
from pyengine.Utils import Vec2


class PPosition(PositionComponent):
    def __init__(self):
        super(PPosition, self).__init__(Vec2(200, 200), Vec2(0, 0))
        try:
            self.init()
        except AttributeError:
            pass
