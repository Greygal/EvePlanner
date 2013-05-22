__author__ = 'apodoprigora'


class TreeSkillGroup(object):
    def __init__(self, group_id, group_name):
        self.__group_id = group_id
        self.__group_name = group_name

    @property
    def id(self):
        return self.__group_id

    @property
    def name(self):
        return self.__group_name

    def __str__(self):
        return "Group(id = %d, name = %s" % (self.id, self.name)


