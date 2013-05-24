import configparser
from tkinter import *
from tkinter import ttk

from eveapi_wrapper.character_wrapper import CharacterWrapper
from eveapi import eveapi
from eveapi.cache_handler import CacheHandler
from eveapi_wrapper.eve_wrapper import EveWrapper
from eveapi_wrapper.server_wrapper import ServerWrapper
from ui.skill_tree_frame import SkillTreeFrame


__author__ = 'stkiller'


class EvePlanner(object):
    def __init__(self):
        super().__init__()
        self.__key, self.__code = self.__read_configuration()
        self.__api = eveapi.EVEAPIConnection(cacheHandler=CacheHandler(debug=True))
        self.__auth = self.__api.auth(keyID=self.__key, vCode=self.__code)
        self.__characters = self.__auth.account.Characters()
        self.__me = self.__auth.character(self.__characters.characters[0].characterID)
        self.__eve_wrapper = EveWrapper(self.__api)
        self.__char_wrapper = CharacterWrapper(self.__me, self.__eve_wrapper)
        self.__server_wrapper = ServerWrapper(self.__api)
        self.__root = Tk()
        self.__skill_queue = StringVar(master=self.__root, value="No data yet")
        self.__init_ui()


    def __read_configuration(self):
        parser = configparser.ConfigParser()
        parser.read('../config/api_auth.config')
        return parser.get('Auth Config', 'key'), parser.get('Auth Config', 'code')

    def __init_ui(self):
        self.__root.title("Skill queue statistics")
        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure(0, weight=1, minsize=300)

        notebook = ttk.Notebook(master=self.__root)
        notebook.grid(row=0, column=0, sticky="nswe")

        tree_frame = SkillTreeFrame(self.__char_wrapper, master=self.__root)
        notebook.add(tree_frame, text="Skill tree")

        self.__root.mainloop()


if __name__ == "__main__":
    EvePlanner()
