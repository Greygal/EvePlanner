from tkinter import Menu

__author__ = 'stkiller'


class EveMenu(Menu):
    def __init__(self, cache_handler, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self._cache_handler = cache_handler
        self._init_menu()

    def _init_menu(self):
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label="Delete cache", command=self._cache_handler.purge_all_caches)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.add_cascade(label="File", menu=file_menu)
