from pyengine.Widgets import ProgressBar
from pyengine.Utils import Vec2


class Progress(ProgressBar):
    def __init__(self):
        super(Progress, self).__init__(Vec2(400, 100), Vec2(200, 20))
        try:
            self.init()
        except AttributeError:
            pass
