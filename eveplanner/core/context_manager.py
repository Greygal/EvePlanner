from eveplanner.eveapi_wrapper.character_wrapper import CharacterWrapper
from eveplanner.eveapi_wrapper.eve_wrapper import EveWrapper
from eveplanner.eveapi_wrapper.server_wrapper import ServerWrapper

__author__ = 'apodoprigora'


class ContextManager(object):
    def __init__(self):
        super().__init__()
        self._auth_manager = None
        self._api = None
        self._auth = None
        self._characters = None
        self._me = None
        self._eve_wrapper = None
        self._char_wrapper = None
        self._server_wrapper = None

        self._listeners = []

    def set_current_data(self, auth_manager):
        self._auth_manager = auth_manager
        self._eve_wrapper = EveWrapper(self.api)
        self._char_wrapper = CharacterWrapper(self.current_character, self.eve_wrapper)
        self._server_wrapper = ServerWrapper(self.api)
        self._notify_listeners()

    def _notify_listeners(self):
        for listener in self._listeners:
            try:
                listener.context_changed()
            except AttributeError:
                pass

    def register_listener(self, listener):
        """
        Appends the object as a listener. The appended object should contain method context_changed
        """
        self._listeners.append(listener)

    @property
    def cache_handler(self):
        return self._auth_manager.cache_handler

    @property
    def api(self):
        return self._auth_manager.api

    @property
    def auth(self):
        return self._auth_manager.auth

    @property
    def all_characters(self):
        return self._characters

    @property
    def current_character(self):
        return self._me

    @property
    def eve_wrapper(self):
        return self._eve_wrapper

    @property
    def char_wrapper(self):
        return self._char_wrapper

    @property
    def server_wrapper(self):
        return self._server_wrapper
