from pyengine import Window
from pyengine.Utils import Color
from Worlds.Monde import Monde


class Fenetre(Window):
    def __init__(self):
        super(Fenetre, self).__init__(1100, 800, Color(0, 0, 0), title="PyEngine Game", limit_fps=None, update_rate=60, debug=False)
        try:
            self.init()
        except AttributeError:
            pass
        self.monde = Monde(self)
        self.world = self.monde
        self.run()


Fenetre()
