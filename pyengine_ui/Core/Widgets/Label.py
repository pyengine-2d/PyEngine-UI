from PyQt5.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, text, size):
        super(Label, self).__init__(text)
        font = self.font()
        font.setPointSize(size)
        self.setFont(font)
