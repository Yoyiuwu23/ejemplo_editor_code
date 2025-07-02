from .base import BaseHighlighter

class HtmlHighlighter(BaseHighlighter):
    KEYWORDS = [
        "html", "head", "body", "title", "meta", "link", "script", "style", "div", "span", "h1", "h2", "h3",
        "h4", "h5", "h6", "p", "a", "img", "ul", "ol", "li", "table", "tr", "td", "th", "form", "input",
        "button", "br", "hr"
    ]
    COLOR = "#0000FF"
