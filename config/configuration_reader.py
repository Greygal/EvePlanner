import configparser

__author__ = 'apodoprigora'

class ConfigurationReader(object):
    def __init__(self):
        super().__init__()

    def read_configuration(self):
        parser = configparser.ConfigParser()
        parser.read('../config/api_auth.config')
        return parser.get('Auth Config', 'key'), parser.get('Auth Config', 'code')




