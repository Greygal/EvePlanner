from idlelib.WidgetRedirector import WidgetRedirector
from tkinter import Text

__author__ = 'apodoprigora'
class ReadOnlyText(Text):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.redirector = WidgetRedirector(self)
        self.insert = self.redirector.register("insert", lambda *args, **kw: "break")
        self.delete = self.redirector.register("delete", lambda *args, **kw: "break")
