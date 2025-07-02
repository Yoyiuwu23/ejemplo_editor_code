import os
from tkinter import ttk

class ProjectExplorer(ttk.Frame):
    def __init__(self, master, open_file_callback):
        super().__init__(master)
        self.tree = ttk.Treeview(self, show="tree")
        self.tree.pack(fill="both", expand=True)
        self.open_file_callback = open_file_callback
        self.root_path = None  # Guardará la raíz del proyecto
        self.tree.bind("<<TreeviewOpen>>", self.on_open_node)
        self.tree.bind("<Double-1>", self.on_double_click)

    def load_folder(self, folder_path):
        # Limpia el árbol y guarda la raíz
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.root_path = os.path.abspath(folder_path)
        root_node = self.tree.insert("", "end", text=os.path.basename(self.root_path), open=False, values=(self.root_path,))
        self._add_dummy(root_node)

    def _add_dummy(self, node):
        self.tree.insert(node, "end", text="...", values=("DUMMY",))

    def on_open_node(self, event):
        node = self.tree.focus()
        abspath = self.tree.item(node, "values")[0]
        children = self.tree.get_children(node)
        if children:
            first_child = self.tree.item(children[0], "values")[0]
            if first_child == "DUMMY":
                self.tree.delete(children[0])
                self.populate_node(node, abspath)

    def populate_node(self, node, path):
        try:
            for name in sorted(os.listdir(path)):
                abspath = os.path.join(path, name)
                if os.path.isdir(abspath):
                    folder_node = self.tree.insert(node, "end", text=name, open=False, values=(abspath,))
                    self._add_dummy(folder_node)
                else:
                    self.tree.insert(node, "end", text=name, values=(abspath,))
        except PermissionError:
            pass

    def on_double_click(self, event):
        item_id = self.tree.focus()
        abspath = self.tree.item(item_id, "values")[0]
        if abspath != "DUMMY" and os.path.isfile(abspath):
            # Calcula la ruta relativa al proyecto
            if self.root_path:
                relative_path = os.path.relpath(abspath, self.root_path)
            else:
                relative_path = abspath
            self.open_file_callback(abspath, relative_path)
