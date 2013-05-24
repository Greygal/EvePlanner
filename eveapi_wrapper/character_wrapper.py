from eveapi_objects.character.training_skill import TrainingSkill
from .eve_wrapper import EveWrapper

__author__ = 'apodoprigora'


class CharacterWrapper(object):
    def __init__(self, char_auth_api, eve_wrapper):
        self.__auth_api = char_auth_api
        assert isinstance(eve_wrapper, EveWrapper), "You should provide a EveWrapper instance here"
        self.__eve_wrapper = eve_wrapper
        self.__skill_queue = None

    def _ensure_training_data_is_read(self, update_cache):
        if self.__skill_queue is None or update_cache:
            self.__skill_queue = {}
            for skills in self.__auth_api.SkillQueue().skillqueue:
                tree_skill = self.__eve_wrapper.get_skill_by(skills.typeID)
                self.__skill_queue[skills.queuePosition] = TrainingSkill(skills.queuePosition, tree_skill, skills.level, skills.startSP,
                                                                         skills.endSP, skills.startTime, skills.endTime)

    def get_training_queue(self, update_cache=False):
        self._ensure_training_data_is_read(update_cache)
        return list(self.__skill_queue.values())

    def get_character_image(self):
        #http://image.eveonline.com/Character/93329844_512.jpg
        pass
