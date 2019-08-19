from pyengine.Entities import Entity
from Components.Pos import Pos
from Components.Sprite import Sprite
from Components.Anim import Anim


class E(Entity):
    def __init__(self):
        super(E, self).__init__()
        try:
            self.init()
        except AttributeError:
            pass
        self.add_component(Pos())
        self.add_component(Sprite())
        self.add_component(Anim())
