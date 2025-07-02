from .base import BaseHighlighter

class CssHighlighter(BaseHighlighter):
    KEYWORDS = [
        "color", "background", "background-color", "font-size", "font-family", "margin", "padding", "border",
        "width", "height", "display", "position", "top", "left", "right", "bottom", "float", "clear",
        "overflow", "text-align", "vertical-align", "z-index"
    ]
    COLOR = "#B22222"
