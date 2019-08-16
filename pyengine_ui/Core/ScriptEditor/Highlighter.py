from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PyQt5.QtCore import Qt, QRegularExpression, QRegExp


def text_format(color, style=''):
    f = QTextCharFormat()
    f.setForeground(color)
    if 'bold' in style:
        f.setFontWeight(QFont.Bold)
    if 'italic' in style:
        f.setFontItalic(True)
    return f


styles = {
    'keyword': text_format(Qt.blue),
    'operator': text_format(Qt.red),
    'brace': text_format(Qt.darkGray),
    'defclass': text_format(Qt.black, 'bold'),
    'string': text_format(Qt.magenta),
    'string2': text_format(Qt.darkMagenta),
    'comment': text_format(Qt.darkGreen, 'italic'),
    'self': text_format(Qt.black, 'italic'),
    'numbers': text_format(Qt.green),
}
keywords = [
    'and', 'assert', 'break', 'class', 'continue', 'def',
    'del', 'elif', 'else', 'except', 'exec', 'finally',
    'for', 'from', 'global', 'if', 'import', 'in',
    'is', 'lambda', 'not', 'or', 'pass', 'print',
    'raise', 'return', 'try', 'while', 'yield',
    'None', 'True', 'False',
]

operators = [
    '=',
    # Comparison
    '==', '!=', '<', '<=', '>', '>=',
    # Arithmetic
    '\+', '-', '\*', '/', '//', '\%', '\*\*',
    # In-place
    '\+=', '-=', '\*=', '/=', '\%=',
    # Bitwise
    '\^', '\|', '\&', '\~', '>>', '<<',
]

braces = [
    '\{', '\}', '\(', '\)', '\[', '\]',
]


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(Highlighter, self).__init__(parent)
        self.rules = []

        self.rules += [(r'\b%s\b' % w, 0, styles['keyword'])
                       for w in keywords]
        self.rules += [(r'%s' % o, 0, styles['operator'])
                       for o in operators]
        self.rules += [(r'%s' % b, 0, styles['brace'])
                       for b in braces]

        self.rules += [
            (r'\bself\b', 0, styles['self']),

            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, styles['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, styles['string']),

            (r'\bdef\b\s*(\w+)', 1, styles['defclass']),
            # 'class' followed by an identifier
            (r'\bclass\b\s*(\w+)', 1, styles['defclass']),

            (r'#[^\n]*', 0, styles['comment']),

            (r'\b[+-]?[0-9]+[lL]?\b', 0, styles['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, styles['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, styles['numbers']),
        ]


        self.rules = [(QRegularExpression(pat), index, fmt) for (pat, index, fmt) in self.rules]
        self.tri_single = (QRegExp("'''"), 1, styles['string2'])
        self.tri_double = (QRegExp('"""'), 2, styles['string2'])

    def highlightBlock(self, text):
        for exp, nth, style in self.rules:
            match_ite = exp.globalMatch(text)
            while match_ite.hasNext():
                match = match_ite.next()
                self.setFormat(match.capturedStart(nth), match.capturedLength(nth), style)

        self.setCurrentBlockState(0)
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)

        if self.currentBlockState() == in_state:
            return True
        else:
            return False
