from lib_note_text.constant_parameters import ConstantsText
from lib_metods.up_windows import read_from_a_file, writing_in_file
from tkinter import END


class ReadWrite(ConstantsText):
    def __init__(self):
        super().__init__()

    def loading_text(self):
        text_file = read_from_a_file()
        if text_file:
            self.delete('1.0', END)
            self.insert('1.0', text_file)

    def save_text(self):
        text_file = self.get(1.0, END)
        if text_file:
            writing_in_file(text_file)

