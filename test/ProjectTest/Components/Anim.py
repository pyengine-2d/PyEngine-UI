from pyengine.Components import AnimComponent


class Anim(AnimComponent):
    def __init__(self):
        super(Anim, self).__init__(20, ['Images/idle.png', 'Images/sprite0.png', 'Images/test.gif'], False, False)
        try:
            self.init()
        except AttributeError:
            pass
