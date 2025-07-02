import tkinter as tk
import re

class BaseHighlighter:
    KEYWORDS = []
    COLOR = "#000000"

    def __init__(self, text_widget):
        self.text_widget = text_widget
        self._setup_tags()

    def _setup_tags(self):
        self.text_widget.tag_configure("keyword", foreground=self.COLOR)

    def highlight(self, event=None):
        self.text_widget.tag_remove("keyword", "1.0", tk.END)
        if not self.KEYWORDS:
            return
        pattern = r'\b(' + '|'.join(re.escape(word) for word in self.KEYWORDS) + r')\b'
        text = self.text_widget.get("1.0", tk.END)
        for match in re.finditer(pattern, text):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text_widget.tag_add("keyword", start, end)
