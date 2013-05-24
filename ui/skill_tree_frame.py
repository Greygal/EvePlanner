from tkinter import *
from tkinter import ttk
from eveapi_wrapper.character_wrapper import CharacterWrapper

__author__ = 'apodoprigora'


class SkillTreeFrame(ttk.Frame):
    def __init__(self, char_wrapper, master=None, cnf={}, **kw):
        super().__init__(master=master, **kw)
        if not isinstance(char_wrapper, CharacterWrapper):
            raise RuntimeError("There should be a character wrapper")
        self.__char_wrapper = char_wrapper
        self.__skill_name_list = StringVar()
        self.__skill_description = StringVar(value="Please select a skill")
        self._skill_list = []
        self.initialize_widgets()
        self.initialize_self()

    def initialize_widgets(self):
        skill_frame = ttk.Frame(master=self, padding=(3, 3, 3, 3))
        skill_frame.grid(row=0, column=0, sticky="nswe")
        skill_frame.rowconfigure(0, weight=1)
        skill_frame.columnconfigure(0, weight=1)
        skill_frame.columnconfigure(2, minsize=400)

        self.__list_box = Listbox(master=skill_frame, height=10, listvariable=self.__skill_name_list)
        self.__list_box.grid(row=0, column=0, sticky="nswe")

        scrollbar = ttk.Scrollbar(master=skill_frame, orient=VERTICAL, command=self.__list_box.yview)
        scrollbar.grid(row=0, column=1, sticky="nswe")
        self.__list_box.configure(yscrollcommand=scrollbar.set)
        self.__list_box.bind('<<ListboxSelect>>', self.__showPopulation)

        self.__text_label = Text(master=skill_frame)
        self.__text_label.grid(row = 0, column=2, sticky="nswe")
        # self.__text_label.configure(state="disabled")

        ttk.Button(master=self, text="Refresh", command=self.refresh_data).grid(row=1, column=0, columnspan=2, sticky=S)


    def refresh_data(self):
        self._skill_list = self.__char_wrapper.get_training_queue(update_cache=True)

        def get_skill_list_element(skill):
            return "%d. %s" % (skill.position, skill.tree_skill.name)

        self.__skill_name_list.set(tuple([get_skill_list_element(skill) for skill in self._skill_list]))

    def initialize_self(self):
        self.grid(row=0, column=0, sticky="nswe")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def __showPopulation(self, index):
        selection = self.__list_box.curselection()
        self.__text_label.delete("1.0", END)
        self.__text_label.insert("0.0", self._skill_list[int(selection[0])])
