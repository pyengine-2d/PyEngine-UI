from pyengine.Components import SpriteComponent


class Sprite(SpriteComponent):
    def __init__(self):
        super(Sprite, self).__init__("Images/sprite0.png", 1, 0, False, False)
        try:
            self.init()
        except AttributeError:
            pass
