__author__ = 'apodoprigora'
class ServerWrapper(object):
    def __init__(self, api=None):
        self.__api = api

    def set_api(self, api):
        self.__api = api

    def get_server_status(self):
        """
        Returns a tuple (server_open, online_players)
        """
        if not self._initialised():
            return None,None
        status = self.__api.server.ServerStatus()
        return status.serverOpen, status.onlinePlayers

    def _initialised(self):
        return self.__api
