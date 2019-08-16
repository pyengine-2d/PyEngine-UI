from pyengine import Window
from Worlds.Monde import Monde


class Fenetre(Window):
    def __init__(self):
        super(Fenetre, self).__init__(900, 600, title="PyEngine Game", limit_fps=None, update_rate=60, debug=False)
        self.monde = Monde(self)
        self.world = self.monde
    
        self.run()


Fenetre()