from pyengine.Components import PhysicsComponent


class PPhysique(PhysicsComponent):
    def __init__(self):
        super(PPhysique, self).__init__(False, 1, 0, 1, True)
        try:
            self.init()
        except AttributeError:
            pass
