import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from tkinter import ttk
from .project_explorer import ProjectExplorer
from .menu_bar import MenuBar
from .line_numbers import TextLineNumbers
from .syntax_highlighter import get_highlighter_for_file
from file_ops import open_file, save_file
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Editor de Texto")
        self.root.geometry("900x600")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(3, weight=1)  # columna 3 es el área de texto

        # Panel lateral
        self.sidebar = ProjectExplorer(self.root, self.open_file)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Scrollbar vertical compartido
        self.v_scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.v_scrollbar.grid(row=0, column=2, sticky="ns")

        # Área de texto principal (primero crea el área de texto)
        self.text_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, undo=True, font=("Consolas", 12),
            yscrollcommand=self._on_text_scroll
        )
        self.text_area.grid(row=0, column=3, sticky="nsew")

        # Contador de líneas (Canvas), pásale el área de texto
        self.line_numbers = TextLineNumbers(self.root, self.text_area, width=40, bg="#f0f0f0", highlightthickness=0)
        self.line_numbers.grid(row=0, column=1, sticky="ns")

        # Vincula el scrollbar a ambos widgets
        self.v_scrollbar.config(command=self._on_scrollbar)
        self.text_area.config(yscrollcommand=self._on_text_scroll)

        self.current_file = None

        # Resaltador de sintaxis modular
        self.syntax = get_highlighter_for_file(self.text_area, "archivo.py")
        self.text_area.bind("<KeyRelease>", self._on_text_change)
        self.syntax.highlight()

        # Inicializa modo visual
        self.dark_mode = False
        self.set_light_mode()

        # Menú
        self.menu_bar = MenuBar(self)
        self.root.config(menu=self.menu_bar.menu_bar)

        # Otros eventos para actualizar líneas (por si acaso)
        self.text_area.bind("<Button-1>", self._on_text_change)
        self.text_area.bind("<Configure>", self._on_text_change)
        self.text_area.bind("<<Change>>", self._on_text_change)
        self.text_area.bind("<<Modified>>", self._on_text_change)

        self.line_numbers.redraw()

    def _on_text_scroll(self, *args):
        self.v_scrollbar.set(*args)
        self.line_numbers.redraw()

    def _on_scrollbar(self, *args):
        self.text_area.yview(*args)
        self.line_numbers.redraw()

    def _on_text_change(self, event=None):
        self.syntax.highlight()
        self.line_numbers.redraw()

    def new_file(self):
        if self.confirm_unsaved_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.root.title("Mi Editor de Texto - Nuevo archivo")
            self.syntax = get_highlighter_for_file(self.text_area, "archivo.py")
            self.text_area.bind("<KeyRelease>", self._on_text_change)
            self.syntax.highlight()
            self._on_text_change()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            initialdir=os.path.expanduser("~"),
            filetypes=[("Todos los archivos", "*.*")]
        )
        if file_path:
            if self.sidebar.root_path:
                rel_path = os.path.relpath(file_path, self.sidebar.root_path)
            else:
                rel_path = file_path
            self.open_file(file_path, rel_path)

    def open_folder_dialog(self):
        folder_path = filedialog.askdirectory(
            title="Selecciona una carpeta",
            initialdir=os.path.expanduser("~")
        )
        if folder_path:
            self.sidebar.load_folder(folder_path)
            self.root.title(f"Mi Editor de Texto - {os.path.basename(folder_path)}")

    def open_file(self, file_path, relative_path=None):
        content = open_file(file_path)
        if content is not None:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.current_file = file_path
            self.syntax = get_highlighter_for_file(self.text_area, file_path)
            self.text_area.bind("<KeyRelease>", self._on_text_change)
            self.syntax.highlight()
            self._on_text_change()
            if relative_path:
                self.root.title(f"Mi Editor de Texto - {relative_path}")
            else:
                self.root.title(f"Mi Editor de Texto - {file_path}")

    def save_file(self):
        if self.current_file:
            save_file(self.current_file, self.text_area.get(1.0, tk.END))
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialdir=os.path.expanduser("~")
            )
            if file_path:
                save_file(file_path, self.text_area.get(1.0, tk.END))
                self.current_file = file_path
                self.root.title(f"Mi Editor de Texto - {os.path.basename(file_path)}")

    def confirm_unsaved_changes(self):
        if self.text_area.edit_modified():
            respuesta = messagebox.askyesnocancel(
                "Cambios no guardados", "¿Deseas guardar los cambios antes de continuar?"
            )
            if respuesta:  # Sí
                self.save_file()
                return True
            elif respuesta is None:  # Cancelar
                return False
            else:
                return True
        return True

    def show_preferences(self):
        pref_window = tk.Toplevel(self.root)
        pref_window.title("Preferencias de aspecto")
        pref_window.geometry("300x150")
        pref_window.resizable(False, False)

        dark_mode_var = tk.BooleanVar(value=self.dark_mode)

        def apply_theme():
            if dark_mode_var.get():
                self.set_dark_mode()
                self.dark_mode = True
            else:
                self.set_light_mode()
                self.dark_mode = False

        dark_mode_check = tk.Checkbutton(pref_window, text="Modo oscuro", variable=dark_mode_var, command=apply_theme)
        dark_mode_check.pack(pady=30)
        tk.Button(pref_window, text="Cerrar", command=pref_window.destroy).pack(pady=10)

    def set_dark_mode(self):
        self.text_area.config(bg="#1e1e1e", fg="#d4d4d4", insertbackground="#d4d4d4")
        self.line_numbers.config(bg="#232323")
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
                        background="#232323",
                        foreground="#d4d4d4",
                        fieldbackground="#232323")
        style.map('Treeview', background=[('selected', '#44475a')])
        self.root.config(bg="#232323")

    def set_light_mode(self):
        self.text_area.config(bg="white", fg="black", insertbackground="black")
        self.line_numbers.config(bg="#f0f0f0")
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        fieldbackground="white")
        style.map('Treeview', background=[('selected', '#dbeafe')])
        self.root.config(bg="white")

    def show_about(self):
        messagebox.showinfo("Acerca de", "Editor de texto básico con Python y Tkinter.")
