from eveapi_objects.eve.tree_skill import TreeSkill
from eveapi_objects.eve.tree_skill_group import TreeSkillGroup

__author__ = 'apodoprigora'


class EveWrapper(object):
    def __init__(self, api):
        self.api = api
        self.skill_groups = None
        self.all_skills = None
        self.tree = None

    def get_skill_tree(self):
        """
        Returns the whole skill tree : ( Group (groupId, groupName) -> Skill(typeName,groupID,typeID,published)
        """
        if self.tree is None:
            self.tree = self.api.eve.SkillTree()
        return self.tree

    def get_skill_groups(self):
        """
        Returns a list of all skill groups ( Group class )
        """
        if self.skill_groups is None:
            #TODO apodoprigora implement saving groups as dictionary
            result = []
            skill_tree = self.get_skill_tree()
            for group in skill_tree.skillGroups:
                result.append(TreeSkillGroup(group.groupID, group.groupName, group.skills))
            self.skill_groups = result
        return self.skill_groups

    def get_all_skills(self):
        """
        Returns a list of all available skills ( Skill class )
        """
        if self.all_skills is None:
            result = {}
            groups = self.get_skill_groups()
            for group in groups:
                for skill in group.skills:
                    result[skill.typeID] = TreeSkill(skill.typeName, skill.groupID, skill.typeID, skill.description)
            self.all_skills = result
        return self.all_skills.values()

    def get_skill_by(self, skill_type_id):
        if self.all_skills is None:
            self.get_all_skills()
        try:
            return self.all_skills[skill_type_id]
        except KeyError:
            return None



