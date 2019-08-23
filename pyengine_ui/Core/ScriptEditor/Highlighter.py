from PySide2.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor
from PySide2.QtCore import QRegularExpression, QRegExp

import os
import json


def text_format(color, style=''):
    f = QTextCharFormat()
    f.setForeground(color)
    if 'bold' in style:
        f.setFontWeight(QFont.Bold)
    if 'italic' in style:
        f.setFontItalic(True)
    return f


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
    def __init__(self, parent, doc):
        super(Highlighter, self).__init__(doc)
        self.main = parent.parent.parent
        self.parent = parent
        self.styles = {}
        self.update_styles()
        self.rules = []
        self.tri_double = []
        self.tri_single = []
        self.update_rules()

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

    def update_rules(self):
        self.rules = []

        self.rules += [(r'\b%s\b' % w, 0, self.styles['keyword'])
                       for w in keywords]
        self.rules += [(r'%s' % o, 0, self.styles['operator'])
                       for o in operators]
        self.rules += [(r'%s' % b, 0, self.styles['brace'])
                       for b in braces]

        self.rules += [
            (r'\bself\b', 0, self.styles['self']),

            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, self.styles['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, self.styles['string']),

            (r'\bdef\b\s*(\w+)', 1, self.styles['defclass']),
            # 'class' followed by an identifier
            (r'\bclass\b\s*(\w+)', 1, self.styles['defclass']),

            (r'#[^\n]*', 0, self.styles['comment']),

            (r'\b[+-]?[0-9]+[lL]?\b', 0, self.styles['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, self.styles['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, self.styles['numbers']),
        ]

        self.rules = [(QRegularExpression(pat), index, fmt) for (pat, index, fmt) in self.rules]
        self.tri_single = (QRegExp("'''"), 1, self.styles['string2'])
        self.tri_double = (QRegExp('"""'), 2, self.styles['string2'])

    def update_styles(self):
        with open(os.path.join(self.main.theme, "highlighter.json"), 'r') as f:
            dic = json.load(f)

        self.styles = dic["styles"]
        for k, v in self.styles.items():
            if len(v) == 3:
                self.styles[k] = text_format(QColor(v[0], v[1], v[2]))
            else:
                self.styles[k] = text_format(QColor(v[0], v[1], v[2]), v[3])
