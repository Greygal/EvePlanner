from tkinter import *
from tkinter import ttk, messagebox

from eveplanner.ui.skill_tree_frame import SkillTreeFrame
from eveplanner.config.configuration_reader import ConfigurationReader
from eveplanner.context.auth_manager import AuthManager
from eveplanner.context.context_manager import ContextManager
from eveplanner.eveapi.cache_handler import CacheHandler
from eveplanner.ui.character_info import CharacterInfoFrame
from eveplanner.ui.eve_menu import EveMenu


__author__ = 'stkiller'


class EvePlanner(object):
    def __init__(self):
        super().__init__()
        self._root = Tk()
        self._init_access_api()
        self._init_ui()
        self._skill_queue = StringVar(master=self._root, value="No data yet")

    def _init_access_api(self):
        try:
            self._key, self.__code = ConfigurationReader().read_configuration()
        except RuntimeError as re:
            messagebox.showerror("Could not open the configuration file. Please add another key/id pair.")
        self._cache_handler = CacheHandler(debug=True)
        self._context_manager = ContextManager()
        self._auth_manager = AuthManager(cache_handler=self._cache_handler, context_manager=self._context_manager)
        self._auth_manager.set_auth_data(self._key, self.__code)

    def _init_ui(self):
        self._init_root()
        self._init_menus()
        self._init_notebook()

        self._auth_manager.set_selected_character(self._auth_manager.get_all_characters()[0])

        self._root.mainloop()

    def _init_root(self):
        self._root.title("Skill queue statistics")
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)
        self._root.minsize(600, 400)
        self._root.maxsize(600, 400)

    def _init_menus(self):
        self._root.config(menu=EveMenu(self._context_manager, master=self._root))

    def _init_notebook(self):
        notebook = ttk.Notebook(master=self._root)
        notebook.grid(row=0, column=0, sticky="nswe")
        char_frame = CharacterInfoFrame(master=self._root)
        tree_frame = SkillTreeFrame(self._context_manager, master=self._root)
        notebook.add(char_frame, text="Character info")
        notebook.add(tree_frame, text="Skill tree")


if __name__ == "__main__":
    EvePlanner()
