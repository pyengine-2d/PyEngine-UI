from pyengine.Components import PhysicsComponent


class Physique(PhysicsComponent):
    def __init__(self):
        super(Physique, self).__init__(True, 1, 0, 1, True, False)
        try:
            self.init()
        except AttributeError:
            pass
