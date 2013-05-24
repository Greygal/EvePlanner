__author__ = 'apodoprigora'
class ServerWrapper(object):
    def __init__(self, api):
        self.__api = api

    def get_server_status(self):
        """
        Returns a tuple (server_open, online_players)
        """
        status = self.__api.server.ServerStatus()
        return status.serverOpen, status.onlinePlayers
