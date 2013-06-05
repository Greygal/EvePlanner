from tkinter import *
from tkinter import ttk, messagebox

from eveplanner.config.configuration_reader import ConfigurationReader
from eveplanner.eveapi_wrapper.character_wrapper import CharacterWrapper
from eveplanner.eveapi.cache_handler import CacheHandler
from eveplanner.eveapi_wrapper.eve_wrapper import EveWrapper
from eveplanner.eveapi_wrapper.server_wrapper import ServerWrapper
from eveplanner.eveapi import eveapi
from eveplanner.ui.character_info import CharacterInfoFrame
from eveplanner.ui.eve_menu import EveMenu
from eveplanner.ui.skill_tree_frame import SkillTreeFrame


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
        self._api = eveapi.EVEAPIConnection(cacheHandler=self._cache_handler)
        self._auth = self._api.auth(keyID=self._key, vCode=self.__code)
        self._characters = self._auth.account.Characters()
        self._me = self._auth.character(self._characters.characters[0].characterID)
        self._eve_wrapper = EveWrapper(self._api)
        self._char_wrapper = CharacterWrapper(self._me, self._eve_wrapper)
        self._server_wrapper = ServerWrapper(self._api)

    def _init_ui(self):
        self._root.title("Skill queue statistics")
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)
        self._root.minsize(600, 400)
        self._root.maxsize(600, 400)

        notebook = ttk.Notebook(master=self._root)
        notebook.grid(row=0, column=0, sticky="nswe")

        self._root.config(menu=EveMenu(self._cache_handler, master=self._root))

        char_frame = CharacterInfoFrame(master=self._root)
        notebook.add(char_frame, text="Character info")

        tree_frame = SkillTreeFrame(self._char_wrapper, master=self._root)
        notebook.add(tree_frame, text="Skill tree")

        self._root.mainloop()
