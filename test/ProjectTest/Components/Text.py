from pyengine.Components import TextComponent
from pyengine.Utils import Color, Font


class Text(TextComponent):
    def __init__(self):
        super(Text, self).__init__("Michel est pas mort !", Color(0, 0, 0), Font("arial", 15, True, True, True), scale=1)
        try:
            self.init()
        except AttributeError:
            pass
