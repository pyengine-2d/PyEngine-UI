from pyengine.Components import ControlComponent
from pyengine import ControlType


class Controle(ControlComponent):
    def __init__(self):
        super(Controle, self).__init__(ControlType.FOURDIRECTION, 10)
        try:
            self.init()
        except AttributeError:
            pass