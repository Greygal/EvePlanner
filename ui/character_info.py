from tkinter import ttk, PhotoImage, Tk
from urllib.request import urlopen
import base64

__author__ = 'stkiller'


class CharacterInfoFrame(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self._init_widgets()

    def _init_widgets(self):
        URL = "http://image.eveonline.com/Character/93329844_512.jpg"
        u = urlopen(URL)
        raw_data = u.read()
        u.close()
        b64_data = base64.encodebytes(raw_data)
        image = PhotoImage(data=b64_data)
        label = ttk.Label(master=self, image=image)
        label.pack()

if __name__ == "__main__":
    raise RuntimeError("To not use this class, it's broken !")
