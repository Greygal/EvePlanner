import ConfigParser
import time
from eveapi import eveapi

__author__ = 'stkiller'

parser = ConfigParser.ConfigParser()
parser.read('../config/api_auth.config')
YOUR_KEYID = parser.get('Auth Config', 'key')
YOUR_VCODE = parser.get('Auth Config', 'code')

api = eveapi.EVEAPIConnection()
auth = api.auth(keyID=YOUR_KEYID, vCode=YOUR_VCODE)
characters = auth.account.Characters()
me = auth.character(characters.characters[0].characterID)


def print_character_skills():
    # Now that we have a character context, we can display skills trained on
    # a character. First we have to get the skill tree. A real application
    # would cache this data; all objects returned by the api interface can be
    # pickled.
    skilltree = api.eve.SkillTree()
    # Now we have to fetch the charactersheet.
    # Note that the call below is identical to:
    #
    #   acc.char.CharacterSheet(characterID=your_character_id)
    #
    # But, as explained above, the context ("me") we created automatically takes
    # care of adding the characterID parameter and /char folder attribute.
    sheet = me.CharacterSheet()
    # This list should look familiar. They're the skillpoints at each level for
    # a rank 1 skill. We could use the formula, but this is much simpler :)
    sp = [0, 250, 1414, 8000, 45255, 256000]
    total_sp = 0
    total_skills = 0
    # Now the fun bit starts. We walk the skill tree, and for every group in the
    # tree...
    for g in skilltree.skillGroups:

        skills_trained_in_this_group = False

        # ... iterate over the skills in this group...
        for skill in g.skills:

            # see if we trained this skill by checking the character sheet object
            trained = sheet.skills.Get(skill.typeID, False)
            if trained:
                # yep, we trained this skill.

                # print the group name if we haven't done so already
                if not skills_trained_in_this_group:
                    print g.groupName
                    skills_trained_in_this_group = True

                # and display some info about the skill!
                print "- %s Rank(%d) - SP: %d/%d - Level: %d" % \
                      (skill.typeName, skill.rank, trained.skillpoints, (skill.rank * sp[trained.level]), trained.level)
                total_skills += 1
                total_sp += trained.skillpoints


    # And to top it off, display totals.
    print "You currently have %d skills and %d skill points" % (total_skills, total_sp)


def get_skill_by(type_id):
    skill_tree = api.eve.SkillTree()
    for group in skill_tree.skillGroups:
        for skill in group.skills:
            if skill.typeID == type_id:
                return skill.typeName, skill.description

    return None


training = me.SkillInTraining()
currentrly_training = training.skillInTraining == 1
print("Current training : %s" % currentrly_training)
if currentrly_training:
    print("Skill name : %s, training to level %d, will end at %s" % (get_skill_by(training.trainingTypeID)[0], training.trainingToLevel,
                                                                     time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                   time.localtime(training.trainingEndTime))))

print
skill_queue = me.SkillQueue()
for skill in skill_queue.skillqueue:
    print(get_skill_by(skill.typeID))
    print("Skill level %d" % skill.level)
    print("Start time : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(skill.startTime)))
    print("End time : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(skill.endTime)))
    print

# skill_tree = api.eve.SkillTree

