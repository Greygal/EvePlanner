__author__ = 'apodoprigora'


class TreeSkill(object):
    def __init__(self, typeName, groupID, typeID, description):
        self.__type_name = typeName
        self.__group_id = groupID
        self.__type_id = typeID
        self.__description = description

    @property
    def name(self):
        return self.__type_name

    @property
    def group_id(self):
        return self.__group_id

    @property
    def id(self):
        return self.__type_id

    @property
    def description(self):
        return self.__description

    def __str__(self):
        return "Skill(id = %d, name = %s, group id = %d)" % (self.id, self.name, self.group_id)


