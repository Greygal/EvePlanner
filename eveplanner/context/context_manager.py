from eveplanner.context.context_data import ContextData

__author__ = 'apodoprigora'


class ContextManager(object):
    def __init__(self):
        super().__init__()
        self._listeners = []
        self._context_data = ContextData(self)

    def set_current_data(self, auth_manager):
        self._context_data.set_current_data(auth_manager)
        self._notify_listeners()

    def _notify_listeners(self):
        print("Notifying %d listeners" % len(self._listeners))
        for listener in self._listeners:
            print("Notifying listener : %s" % listener.__class__.__name__)
            try:
                listener.context_changed(self._context_data)
            except AttributeError:
                pass
        for listener in self._listeners:
            try:
                listener.context_change_ready()
            except AttributeError:
                pass

    def register_listener(self, listener):
        """
        Appends the object as a listener. The appended object should contain method context_changed
        """
        self._listeners.append(listener)
