from tkinter import Tk
from editor.text_editor import TextEditor

def main():
    root = Tk()
    app = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 