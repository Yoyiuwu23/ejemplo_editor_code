import tkinter as tk

class TextLineNumbers(tk.Canvas):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.textwidget = text_widget
        self.textwidget.bind("<KeyRelease>", self.redraw)
        self.textwidget.bind("<Button-1>", self.redraw)
        self.textwidget.bind("<Configure>", self.redraw)
        self.textwidget.bind("<FocusIn>", self.redraw)
        self.textwidget.bind("<FocusOut>", self.redraw)
        self.textwidget.bind("<<Change>>", self.redraw)
        self.textwidget.bind("<<Modified>>", self.redraw)
        self.redraw()

    def redraw(self, event=None):
        self.delete("all")
        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill='#888888')
            i = self.textwidget.index(f"{i}+1line")

    def yview(self, *args):
        # Permite que el contador responda al scroll
        self.yview_moveto(args[0])
