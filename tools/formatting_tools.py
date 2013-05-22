import time

__author__ = 'stkiller'
from constants import *


class FormattingTools(object):
    def get_formatted_time(self, time_to_format):
        return time.strftime(TIME_FORMAT, time.localtime(time_to_format))
