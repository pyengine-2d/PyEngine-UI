from pyengine.Entities import Entity
from Components.Position import Position
from Components.Sprite import Sprite


class Joueur(Entity):
    def __init__(self):
        super(Joueur, self).__init__()
        self.add_component(Position())
        self.add_component(Sprite())
    print('test')
    print('Génial !')
