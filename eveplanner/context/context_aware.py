from abc import ABCMeta, abstractmethod
from eveplanner.context.context_manager import ContextManager

__author__ = 'stkiller'


class ContextAware(object):
    __metaclass__ = ABCMeta

    def __init__(self, context_manager):
        super().__init__()
        if not isinstance(context_manager, ContextManager):
            raise RuntimeError("You should provide a valid ContextManager instance here")
        self._context_manager = context_manager

    @abstractmethod
    def context_changed(self):
        pass


