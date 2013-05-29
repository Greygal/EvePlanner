from abc import ABCMeta, abstractmethod

__author__ = 'stkiller'


class ContextAware(object):
    __metaclass__ = ABCMeta

    def __init__(self, context_manager):
        super().__init__()
        self._context_manager = context_manager
        self._context_manager.register_listener(self)

    @abstractmethod
    def context_changed(self, context_data):
        pass

    @abstractmethod
    def context_change_ready(self):
        pass


