from eveapi_objects.eve.tree_skill import TreeSkill
from eveapi_objects.eve.tree_skill_group import TreeSkillGroup

__author__ = 'apodoprigora'


class EveWrapper(object):
    def __init__(self, api=None):
        self._api = api
        self._skill_groups = None
        self._skills = None
        self._skills_by_group = None
        self._tree = None

    def set_api(self, api):
        self._api = api

    def _get_skill_tree(self):
        """
        Returns the whole skill tree : ( Group (groupId, groupName) -> Skill(typeName,groupID,typeID,published)
        """
        if not self._api:
            return None
        if self._tree is None:
            self._tree = self._api.eve.SkillTree()
        return self._tree

    def read_skill_tree(self):
        """
        Returns a list of all skill groups ( Group class )
        """
        if self._skill_groups is None:
            self._skill_groups = {}
            self._skills = {}
            self._skills_by_group = {}
            skill_tree = self._get_skill_tree()
            for group in skill_tree.skillGroups:
                if group.groupID not in self._skill_groups:
                    self._skill_groups[group.groupID] = TreeSkillGroup(group.groupID, group.groupName)
                    self._skills_by_group[group.groupID] = []
                for skill in group.skills:
                    tree_skill = TreeSkill(skill.typeName, skill.groupID, skill.typeID, skill.description)
                    self._skills[skill.typeID] = tree_skill
                    self._skills_by_group[group.groupID].append(tree_skill)

        if self._skill_groups is None or self._skills is None:
            raise RuntimeError("The data wasn't loaded, something is wrong!")

    def _ensure_data_is_read(self, update_cache):
        if self._skills is None or update_cache:
            self.read_skill_tree()

    def get_skills(self, update_cache=False):
        """
        Returns a list of all available skills ( TreeSkill class )
        """
        self._ensure_data_is_read(update_cache)
        return list(self._skills.values())

    def get_groups(self, update_cache=False):
        """
        Returns a list of all available skill groups (TreeSkillGroup class)
        """
        self._ensure_data_is_read(update_cache)
        return list(self._skill_groups.values())

    def get_skill_groups(self, update_cache=False):
        """
        Returns a list of all available skill groups ( TreeSkillGroup class )
        """
        self._ensure_data_is_read(update_cache)
        return list(self._skill_groups.values())

    def get_skill_by(self, skill_id, update_cache=False):
        """
        Returns TreeSkill that has specified id, None if nothing is found
        """
        self._ensure_data_is_read(update_cache)
        if skill_id in list(self._skills.keys()):
            return self._skills[skill_id]
        else:
            return None

    def get_group_by(self, group_id, update_cache=False):
        """
        Returns TreeSkillGroup that has the specified id, None if nothing is found
        """
        self._ensure_data_is_read(update_cache)
        if group_id in list(self._skill_groups.keys()):
            return self._skill_groups[group_id]
        else:
            return None

    def get_all_group_skills(self, group_id, update_cache=False):
        """
        Return a list of all skills from the group with specified id
        """
        self._ensure_data_is_read(update_cache)
        if group_id in list(self._skills_by_group.keys()):
            return self._skills_by_group[group_id]




