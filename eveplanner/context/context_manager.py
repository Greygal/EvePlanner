from eveplanner.context.context_data import ContextData

__author__ = 'apodoprigora'


class ContextManager(object):
    def __init__(self):
        super().__init__()
        self._context_data = ContextData(self)
        self._listeners = []

    def set_current_data(self, auth_manager):
        self._context_data.set_current_data(auth_manager)
        self._notify_listeners()

    def _notify_listeners(self):
        for listener in self._listeners:
            try:
                listener.context_changed(self._context_data)
            except AttributeError:
                pass

    def register_listener(self, listener):
        """
        Appends the object as a listener. The appended object should contain method context_changed
        """
        self._listeners.append(listener)
