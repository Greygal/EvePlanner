import ConfigParser
import time
from eveapi import eveapi
from cache_handler import CacheHandler

__author__ = 'stkiller'

parser = ConfigParser.ConfigParser()
parser.read('../config/api_auth.config')
YOUR_KEYID = parser.get('Auth Config', 'key')
YOUR_CODE = parser.get('Auth Config', 'code')

api = eveapi.EVEAPIConnection(cacheHandler=CacheHandler(debug=False))
auth = api.auth(keyID=YOUR_KEYID, vCode=YOUR_CODE)
characters = auth.account.Characters()
me = auth.character(characters.characters[0].characterID)


def get_skill_by(type_id):
    skill_tree = api.eve.SkillTree()
    for group in skill_tree.skillGroups:
        skill = group.skills.Get(type_id, None)
        if skill:
            return str(skill.typeName), str(skill.description)
    return None


training = me.SkillInTraining()
currently_training = training.skillInTraining == 1
if currently_training:
    print("Training now:")
    print("Skill name : %s" % get_skill_by(training.trainingTypeID)[0])
    print("Training to level :%d" % training.trainingToLevel)
    print("Will end at :%s" %
          time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(training.trainingEndTime)))
else:
    print("Nothing training now")

print
skill_queue = me.SkillQueue()
for skill in skill_queue.skillqueue:
    name, description = get_skill_by(skill.typeID)
    print("Skille name : %s\nSkill description : %s" % (name, description))
    print("Skill level %d" % skill.level)
    print("Start time : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(skill.startTime)))
    print("End time : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(skill.endTime)))
    print

# skill_tree = api.eve.SkillTree

