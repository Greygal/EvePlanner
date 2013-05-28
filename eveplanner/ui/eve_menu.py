from tkinter import Menu

__author__ = 'stkiller'


class EveMenu(Menu):
    def __init__(self, context_manager, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self._cache_handler = None
        self._context_manager = context_manager
        self._context_manager.register_listener(self)
        self._init_menu()

    def context_changed(self):
        self._cache_handler = self._context_manager.cache_handler

    def _purge_cached(self):
        if self._cache_handler:
            self._cache_handler.purge_all_caches()

    def _init_menu(self):
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label="Delete cache", command=self._purge_cached)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.add_cascade(label="File", menu=file_menu)
