from tkinter import Scrollbar
from tkinter import BOTH, LEFT, Y
from lib_class_menu import MenuObj
from lib_class_note_text import NoteText

from lib_window.constant_parameters import ConstantsWin


class CreateWindow(ConstantsWin):

    def __init__(self):
        super().__init__()

        self.note_text = NoteText()
        self.note_text.pack(fill=BOTH, expand=1, side=LEFT)

        self.scroll = Scrollbar(self, command=self.note_text.yview)
        self.scroll.pack(side=LEFT, fill=Y)
        self.note_text.config(yscrollcommand=self.scroll.set)
        self.window_menu = MenuObj(self)
        self.config(menu=self.window_menu)
