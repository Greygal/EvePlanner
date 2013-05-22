__author__ = 'apodoprigora'


class TreeSkillGroup(object):
    def __init__(self, group_id, group_name, group_skills):
        self.__group_id = group_id
        self.__group_name = group_name
        self.__group_skills = group_skills

    @property
    def id(self):
        return self.__group_id

    @property
    def name(self):
        return self.__group_name

    @property
    def skills(self):
        return self.__group_skills

    def __str__(self):
        return "Group(id = %d, name = %s, skills number = %d" % (self.id, self.name, len(self.skills))


