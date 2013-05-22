import ConfigParser
import time
from character_wrapper import CharacterWrapper
from eveapi import eveapi
from cache_handler import CacheHandler
from eveapi_wrapper.eve_wrapper import EveWrapper

__author__ = 'stkiller'

parser = ConfigParser.ConfigParser()
parser.read('../config/api_auth.config')
YOUR_KEYID = parser.get('Auth Config', 'key')
YOUR_CODE = parser.get('Auth Config', 'code')

api = eveapi.EVEAPIConnection(cacheHandler=CacheHandler(debug=False))
auth = api.auth(keyID=YOUR_KEYID, vCode=YOUR_CODE)
characters = auth.account.Characters()
me = auth.character(characters.characters[0].characterID)
eve_wrapper = EveWrapper(api)
char_wrapper = CharacterWrapper(me, eve_wrapper)

for skill in char_wrapper.get_training_queue():
    print(skill)

