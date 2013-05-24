from eveapi_objects.eve.tree_skill import TreeSkill
from eveapi_objects.eve.tree_skill_group import TreeSkillGroup

__author__ = 'apodoprigora'


class EveWrapper(object):
    def __init__(self, api):
        self.__api = api
        self.__skill_groups = None
        self.__skills = None
        self.__skills_by_group = None
        self.__tree = None

    def __get_skill_tree(self):
        """
        Returns the whole skill tree : ( Group (groupId, groupName) -> Skill(typeName,groupID,typeID,published)
        """
        if self.__tree is None:
            self.__tree = self.__api.eve.SkillTree()
        return self.__tree

    def read_skill_tree(self):
        """
        Returns a list of all skill groups ( Group class )
        """
        if self.__skill_groups is None:
            self.__skill_groups = {}
            self.__skills = {}
            self.__skills_by_group = {}
            skill_tree = self.__get_skill_tree()
            for group in skill_tree.skillGroups:
                if group.groupID not in self.__skill_groups:
                    self.__skill_groups[group.groupID] = TreeSkillGroup(group.groupID, group.groupName)
                    self.__skills_by_group[group.groupID] = []
                for skill in group.skills:
                    tree_skill = TreeSkill(skill.typeName, skill.groupID, skill.typeID, skill.description)
                    self.__skills[skill.typeID] = tree_skill
                    self.__skills_by_group[group.groupID].append(tree_skill)

        if self.__skill_groups is None or self.__skills is None:
            raise RuntimeError("The data wasn't loaded, something is wrong!")

    def __ensure_data_is_read(self, update_cache):
        if self.__skills is None or update_cache:
            self.read_skill_tree()

    def get_skills(self, update_cache=False):
        """
        Returns a list of all available skills ( TreeSkill class )
        """
        self.__ensure_data_is_read(update_cache)
        return list(self.__skills.values())

    def get_groups(self, update_cache=False):
        """
        Returns a list of all available skill groups (TreeSkillGroup class)
        """
        self.__ensure_data_is_read(update_cache)
        return list(self.__skill_groups.values())

    def get_skill_groups(self, update_cache=False):
        """
        Returns a list of all available skill groups ( TreeSkillGroup class )
        """
        self.__ensure_data_is_read(update_cache)
        return list(self.__skill_groups.values())

    def get_skill_by(self, skill_id, update_cache=False):
        """
        Returns TreeSkill that has specified id, None if nothing is found
        """
        self.__ensure_data_is_read(update_cache)
        if skill_id in list(self.__skills.keys()):
            return self.__skills[skill_id]
        else:
            return None

    def get_group_by(self, group_id, update_cache=False):
        """
        Returns TreeSkillGroup that has the specified id, None if nothing is found
        """
        self.__ensure_data_is_read(update_cache)
        if group_id in list(self.__skill_groups.keys()):
            return self.__skill_groups[group_id]
        else:
            return None

    def get_all_group_skills(self, group_id, update_cache=False):
        """
        Return a list of all skills from the group with specified id
        """
        self.__ensure_data_is_read(update_cache)
        if group_id in list(self.__skills_by_group.keys()):
            return self.__skills_by_group[group_id]




