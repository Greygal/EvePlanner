from eveapi import eveapi
from eveapi.cache_handler import CacheHandler
from eveapi_wrapper.character_wrapper import CharacterWrapper
from eveapi_wrapper.eve_wrapper import EveWrapper
from eveapi_wrapper.server_wrapper import ServerWrapper

__author__ = 'apodoprigora'
class ContextManager(object):
    def __init__(self):
        super().__init__()
        self._key = None
        self._code = None
        self._character = None
        self._cache_handler = CacheHandler(debug=True)
        self._api = None
        self._auth = None
        self._characters = None
        self._me = None
        self._eve_wrapper = None
        self._char_wrapper = None
        self._server_wrapper = None

        self._listeners = []

    def set_current_data(self, key, code, character_code):
        self._key = key
        self._code = code
        self._character = character_code
        self._api = eveapi.EVEAPIConnection(cacheHandler=self._cache_handler)
        self._auth = self._api.auth(keyID=self._key, vCode=self._code)
        self._characters = self._auth.account.Characters()
        self._me = self._auth.character(self._character)
        self._eve_wrapper = EveWrapper(self._api)
        self._char_wrapper = CharacterWrapper(self._me, self._eve_wrapper)
        self._server_wrapper = ServerWrapper(self._api)
        self._notify_listeners()

    def _notify_listeners(self):
        for listener in self._listeners:
            try:
                listener.context_changed()
            except AttributeError:
                pass

    def register_listener(self, listener):
        self._listeners.append(listener)

    @property
    def get_cache_handler(self):
        return self._cache_handler

    @property
    def get_api(self):
        return self._api

    @property
    def get_auth(self):
        return self._auth

    @property
    def get_characters(self):
        return self._characters

    @property
    def get_current_character(self):
        return self._me

    @property
    def get_eve_wrapper(self):
        return self._eve_wrapper

    @property
    def get_char_wrapper(self):
        return self._char_wrapper

    @property
    def get_server_wrapper(self):
        return self._server_wrapper
