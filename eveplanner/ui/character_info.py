import io
from tkinter import ttk, Tk
from urllib.request import urlopen
from PIL import ImageTk, Image
from eveplanner.context.context_aware import ContextAware

__author__ = 'stkiller'


class CharacterInfoFrame(ttk.Frame, ContextAware):
    def __init__(self, context_manager, master=None, **kw):
        ttk.Frame.__init__(self, master, **kw)
        ContextAware.__init__(self, context_manager)
        self._image = None
        self._init_self()
        self._init_widgets()

    def context_changed(self, context_data):
        #TODO implement this when avatar will be loaded correctly
        pass


    def _init_self(self):
        self.grid(row=0, column=0, sticky="nswe")
        self.rowconfigure(0, weight=1, minsize=250)
        self.columnconfigure(0, weight=1, minsize=300)

    def _init_image(self):
        URL = "http://image.eveonline.com/Character/93329844_128.jpg"
        image_bytes = urlopen(URL).read()
        # internal data file
        data_stream = io.BytesIO(image_bytes)
        # open as a PIL image object
        pil_image = Image.open(data_stream)
        # convert PIL image object to Tkinter PhotoImage object
        self._image = ImageTk.PhotoImage(pil_image)

    def _init_widgets(self):
        self._init_image()
        label = ttk.Label(master=self, image=self._image)
        label.grid(row=0, column=0, sticky="nw")
        label.rowconfigure(0, weight=1)
        label.columnconfigure(0, weight=1)


if __name__ == "__main__":
    root = Tk()
    frame = CharacterInfoFrame(master=root)
    frame.master.mainloop()

