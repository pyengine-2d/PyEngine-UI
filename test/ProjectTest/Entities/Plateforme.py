from pyengine.Entities import Entity
from Components.Pposition import PPosition
from Components.Sprite import Sprite
from Components.Pphysique import PPhysique


class Plateforme(Entity):
    def __init__(self):
        super(Plateforme, self).__init__()
        try:
            self.init()
        except AttributeError:
            pass
        self.add_component(PPosition())
        self.add_component(Sprite())
        self.add_component(PPhysique())
