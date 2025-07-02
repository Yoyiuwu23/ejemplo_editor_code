from .base import BaseHighlighter

class JavascriptHighlighter(BaseHighlighter):
    KEYWORDS = [
        "break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else",
        "export", "extends", "finally", "for", "function", "if", "import", "in", "instanceof", "let", "new",
        "return", "super", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with", "yield",
        "enum", "await", "null", "true", "false"
    ]
    COLOR = "#e36209"
