from pyengine.Entities import Entity
from Components.Position import Position
from Components.Sprite import Sprite
from Components.Controle import Controle


class Joueur(Entity):
    def __init__(self):
        super(Joueur, self).__init__()
        try:
            self.init()
        except AttributeError:
            pass
        self.add_component(Position())
        self.add_component(Sprite())
        self.add_component(Controle())
    
    def init(self):
        print("INITIALISATION")
