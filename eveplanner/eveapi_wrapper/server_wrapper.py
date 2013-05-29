from eveplanner.context.context_aware import ContextAware

__author__ = 'apodoprigora'


class ServerWrapper(ContextAware):
    def __init__(self, context_manager):
        ContextAware.__init__(self, context_manager)
        self._api = None

    def context_changed(self, context_data):
        self._api = context_data.api


    def set_api(self, api):
        self._api = api

    def get_server_status(self):
        """
        Returns a tuple (server_open, online_players)
        """
        if not self._initialised():
            return None, None
        status = self._api.server.ServerStatus()
        return status.serverOpen, status.onlinePlayers

    def _initialised(self):
        return self._api
