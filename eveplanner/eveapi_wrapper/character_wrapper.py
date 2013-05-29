from eveplanner.context.context_aware import ContextAware
from eveplanner.eveapi_objects.character.training_skill import TrainingSkill

__author__ = 'apodoprigora'


class CharacterWrapper(ContextAware):
    def __init__(self, context_manager):
        ContextAware.__init__(self, context_manager=context_manager)
        self.__auth_api = None
        self.__eve_wrapper = None
        self.__skill_queue = None

    def context_changed(self, context_data):
        self.__auth_api = context_data.auth
        self.__eve_wrapper = context_data.eve_wrapper

    def _ensure_training_data_is_read(self, update_cache):
        if self.__skill_queue is None or update_cache:
            self.__skill_queue = {}
            for skills in self.__auth_api.SkillQueue().skillqueue:
                tree_skill = self.__eve_wrapper.get_skill_by(skills.typeID)
                self.__skill_queue[skills.queuePosition] = TrainingSkill(skills.queuePosition, tree_skill, skills.level, skills.startSP,
                                                                         skills.endSP, skills.startTime, skills.endTime)

    def get_training_queue(self, update_cache=False):
        if not self._ensure_initialised():
            print("[CharWrapper] not initialized")
            return []
        self._ensure_training_data_is_read(update_cache)
        return list(self.__skill_queue.values())

    def _ensure_initialised(self):
        return self.__auth_api and self.__eve_wrapper

    def get_character_image(self):
        #http://image.eveonline.com/Character/93329844_512.jpg
        pass
