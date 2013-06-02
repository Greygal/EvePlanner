from eveplanner.eveapi.cache_handler import CacheHandler

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
