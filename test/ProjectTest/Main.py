from pyengine import Window
from pyengine.Utils import Color
from Worlds.Monde import Monde


class Fenetre(Window):
    def __init__(self):
        super(Fenetre, self).__init__(900, 600, Color(255, 255, 255), title="PyEngine Game", limit_fps=None, update_rate=60, debug=False)
        try:
            self.init()
        except AttributeError:
            pass
        self.monde = Monde(self)
        self.world = self.monde
        self.run()


Fenetre()
