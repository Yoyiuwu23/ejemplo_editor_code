import os
from .python import PythonHighlighter
from .html import HtmlHighlighter
from .css import CssHighlighter
from .javascript import JavascriptHighlighter
from .sql import SqlHighlighter
from .c import CHighlighter
from .cpp import CppHighlighter
from .csharp import CSharpHighlighter

EXTENSION_MAP = {
    ".py": PythonHighlighter,
    ".html": HtmlHighlighter,
    ".htm": HtmlHighlighter,
    ".css": CssHighlighter,
    ".js": JavascriptHighlighter,
    ".sql": SqlHighlighter,
    ".c": CHighlighter,
    ".h": CHighlighter,
    ".cpp": CppHighlighter,
    ".cc": CppHighlighter,
    ".cxx": CppHighlighter,
    ".hpp": CppHighlighter,
    ".cs": CSharpHighlighter,
}


def get_highlighter_for_file(text_widget, file_path):
    ext = os.path.splitext(file_path)[1].lower()
    highlighter_class = EXTENSION_MAP.get(ext, PythonHighlighter)  # Por defecto Python
    return highlighter_class(text_widget)
