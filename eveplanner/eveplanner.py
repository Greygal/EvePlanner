import configparser
from tkinter import *
from tkinter import ttk

from eveapi_wrapper.character_wrapper import CharacterWrapper
from eveapi import eveapi
from eveapi.cache_handler import CacheHandler
from eveapi_wrapper.eve_wrapper import EveWrapper
from eveapi_wrapper.server_wrapper import ServerWrapper


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

    def __refresh_statistics(self):
        if not self.__skill_queue:
            return None
        res = ""
        for skill in self.__char_wrapper.get_training_queue():
            res += str(skill)
            res += "\n\n"
        self.__skill_queue.set(res)

    def __init_ui(self):
        self.__root.title("Skill queue statistics")

        mainframe = ttk.Frame(self.__root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        ttk.Label(mainframe, textvariable=self.__skill_queue).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Refresh", command=self.__refresh_statistics).grid(column=3, row=3, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.__root.mainloop()


if __name__ == "__main__":
    EvePlanner()
