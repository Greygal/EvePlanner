from eveplanner.eveapi import eveapi


__author__ = 'stkiller'


class AuthManager(object):
    def __init__(self, cache_handler, context_manager):
        super().__init__()
        self._cache_handler = cache_handler
        self._key = None
        self._code = None
        self._user_id = None
        self._api = None
        self._auth = None
        self._me = None
        self._characters = None
        self._context_manager = context_manager

    def set_auth_data(self, key, code):
        self._key = key
        self._code = code
        self._api = eveapi.EVEAPIConnection(cacheHandler=self._cache_handler)
        self._auth = self._api.auth(keyID=self._key, vCode=self._code)
        self._characters = self._auth.account.Characters()

    def set_selected_character(self, user_id):
        self._user_id = user_id
        self._me = self._auth.character(self._user_id)
        self._context_manager.set_current_data(self)

    def get_all_characters(self):
        if not self._auth:
            raise RuntimeError("Cannot get the list of characters, the key and code weren't provided.")
        return self._characters.characters

    @property
    def cache_handler(self):
        return self._cache_handler

    @property
    def key(self):
        return self._key

    @property
    def code(self):
        return self._code

    @property
    def current_character(self):
        return self._user_id

    @property
    def api(self):
        return self._key

    @property
    def auth(self):
        return self._auth

    @property
    def auth_character(self):
        return self._me
