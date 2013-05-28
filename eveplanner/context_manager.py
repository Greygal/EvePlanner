from eveapi import eveapi
from eveapi.cache_handler import CacheHandler
from eveapi_wrapper.character_wrapper import CharacterWrapper
from eveapi_wrapper.eve_wrapper import EveWrapper
from eveapi_wrapper.server_wrapper import ServerWrapper

__author__ = 'apodoprigora'
class ContextManager(object):
    def __init__(self):
        super().__init__()
        self._cache_handler = CacheHandler(debug=True)
        self._api = None
        self._auth = None
        self._characters = None
        self._me = None
        self._eve_wrapper = None
        self._char_wrapper = None
        self._server_wrapper = None
