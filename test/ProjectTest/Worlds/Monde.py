from pyengine import World
from pyengine.Systems import EntitySystem
from Entities.Joueur import Joueur


class Monde(World):
    def __init__(self, window):
        super(Monde, self).__init__(window, [0, -900])
        try:
            self.init()
        except AttributeError:
            pass
        self.esys = self.get_system(EntitySystem)
        self.esys.add_entity(Joueur())
