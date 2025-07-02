import tkinter as tk

class MenuBar:
    def __init__(self, editor):
        self.editor = editor
        self.menu_bar = tk.Menu(self.editor.root)

        # Menú Archivo
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Nuevo", command=self.editor.new_file)
        file_menu.add_command(label="Abrir archivo", command=self.editor.open_file_dialog)
        file_menu.add_command(label="Abrir carpeta", command=self.editor.open_folder_dialog)
        file_menu.add_command(label="Guardar", command=self.editor.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.editor.root.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=file_menu)

        # Menú Opciones
        options_menu = tk.Menu(self.menu_bar, tearoff=0)
        options_menu.add_command(label="Preferencias", command=self.editor.show_preferences)
        options_menu.add_command(label="Acerca de", command=self.editor.show_about)
        self.menu_bar.add_cascade(label="Opciones", menu=options_menu)
