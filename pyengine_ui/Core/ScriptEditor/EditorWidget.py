from PyQt5.QtWidgets import QPlainTextEdit, QTextEdit
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QTextFormat, QPainter

from pyengine_ui.Core.ScriptEditor.LineAreaWidget import LineAreaWidget


class EditorWidget(QPlainTextEdit):
    def __init__(self, parent):
        super(EditorWidget, self).__init__(parent)
        self.parent = parent
        self.linearea = LineAreaWidget(self)

        self.blockCountChanged.connect(self.update_linearea_width)
        self.updateRequest.connect(self.update_linearea)
        self.cursorPositionChanged.connect(self.highlight_currentline)

        self.update_linearea_width(0)
        self.highlight_currentline()

    def linearea_paintevent(self, event):
        painter = QPainter(self.linearea)
        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        block_nb = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_nb + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.linearea.width(), self.fontMetrics().height(), Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_nb += 1

    def linearea_width(self):
        digits = 1
        maxi = max(1, self.blockCount())
        while maxi >= 10:
            maxi /= 10
            digits += 1

        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def resizeEvent(self, event) -> None:
        super(EditorWidget, self).resizeEvent(event)

        cr = self.contentsRect()
        self.linearea.setGeometry(QRect(cr.left(), cr.top(), self.linearea_width(), cr.height()))

    def update_linearea_width(self, nb):
        self.setViewportMargins(self.linearea_width(), 0, 0, 0)

    def highlight_currentline(self):
        extraselections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            line_color = QColor(Qt.yellow).lighter(160)

            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraselections.append(selection)

        self.setExtraSelections(extraselections)

    def update_linearea(self, rect, nb):
        if nb:
            self.linearea.scroll(0, nb)
        else:
            self.linearea.update(0, rect.y(), self.linearea.width(), rect.height())
            if rect.contains(self.viewport().rect()):
                self.update_linearea_width(0)
