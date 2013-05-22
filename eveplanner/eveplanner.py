import ConfigParser
import time
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

training = me.SkillInTraining()
currently_training = training.skillInTraining == 1
if currently_training:
    print("Training now:")
    print("Skill name : %s" % eve_wrapper.get_skill_by(training.trainingTypeID).name)
    print("Training to level :%d" % training.trainingToLevel)
    print("Will end at :%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(training.trainingEndTime)))
else:
    print("Nothing training now")

print
skill_queue = me.SkillQueue()
for skill in skill_queue.skillqueue:
    tree_skill = eve_wrapper.get_skill_by(skill.typeID)
    print("Skill name : %s" % tree_skill.name)
    print("Skill description : %s" % tree_skill.description)
    print("Skill level: %d" % skill.level)
    print("Start time : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(skill.startTime)))
    print("End time   : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(skill.endTime)))
    print

