from pyengine.Entities import Tilemap
from pyengine.Utils import Vec2


class Tile(Tilemap):
    def __init__(self):
        super(Tile, self).__init__(Vec2(400, 300), "Tilemaps/Tile/level.json", 1)
        try:
            self.init()
        except AttributeError:
            pass
