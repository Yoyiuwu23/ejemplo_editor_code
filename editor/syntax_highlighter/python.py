from .base import BaseHighlighter

class PythonHighlighter(BaseHighlighter):
    KEYWORDS = [
        "def", "class", "import", "from", "as", "if", "elif", "else", "for", "while", "return",
        "in", "try", "except", "finally", "with", "lambda", "pass", "break", "continue", "yield",
        "global", "nonlocal", "assert", "del", "raise", "is", "not", "or", "and", "True", "False", "None"
    ]
    COLOR = "#007F00"
