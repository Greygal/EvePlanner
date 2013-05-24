__author__ = 'stkiller'
from tools.formatting_tools import FormattingTools


class TrainingSkill(object):
    def __init__(self, queue_position, tree_skill, level, start_sp, end_sp, start_time, end_time):
        self.__queue_position = queue_position
        self.__tree_skill = tree_skill
        self.__level = level
        self.__start_sp = start_sp
        self.__end_sp = end_sp
        self.__start_time = start_time
        self.__end_time = end_time
        self.__formatting_tool = FormattingTools()

    @property
    def position(self):
        return self.__queue_position + 1

    @property
    def tree_skill(self):
        return self.__tree_skill

    @property
    def level(self):
        return self.__level

    @property
    def start_sp(self):
        return self.__start_sp

    @property
    def end_sp(self):
        return self.__end_sp

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time

    @property
    def duration_in_minutes(self):
        return (self.end_time - self.start_time) / 60

    @property
    def duration_string(self):
        return "%d:%d" % divmod(self.duration_in_minutes, 60)

    def __get_string_time(self, time):
        return self.__formatting_tool.get_formatted_time(
            time)

    def __str__(self):
        header = ""
        if self.position == 0:
            header += "Currently training :"
        else:
            header += "Training skill at position : %d" % self.position
        return "%s\n%-20s : %s\n%-20s : %d\n%-20s : %s\n%-20s : %s\n%-20s : %s" % (header, "Name",
                                                                                   self.tree_skill.name,
                                                                                   "Training to level",
                                                                                   self.level,
                                                                                   "Start time",
                                                                                   self.__get_string_time(self.start_time),
                                                                                   "End Time",
                                                                                   self.__get_string_time(self.end_time),
                                                                                   "Duration", self.duration_string)




