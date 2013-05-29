from tkinter import Menu
from eveplanner.context.context_aware import ContextAware

__author__ = 'stkiller'


class EveMenu(Menu, ContextAware):
    def __init__(self, context_manager, master=None, cnf={}, **kw):
        Menu.__init__(self, master, cnf, **kw)
        ContextAware.__init__(self, context_manager)
        self._cache_handler = None
        self._context_manager.register_listener(self)
        self._init_menu()

    def context_changed(self, context_data):
        self._cache_handler = context_data.cache_handler

    def _purge_cached(self):
        if self._cache_handler:
            self._cache_handler.purge_all_caches()

    def _init_menu(self):
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label="Delete cache", command=self._purge_cached)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.add_cascade(label="File", menu=file_menu)
