from lib_note_text.change_theme import ChangeTheme
from lib_metods.working_with_db import read_start_parameters_from_db, write_exit_parameters_in_db
from tkinter import StringVar


class ChoiceFont(ChangeTheme):

    font_view = {'Arial': {'font': ('Arial', 12, 'bold')},
                 'Comic Sans MS': {'font': ('Comic Sans MS', 12, 'bold')},
                 'Times New Roman': {'font': ('Times New Roman', 12, 'bold')}}

    def __init__(self):
        super().__init__()
        self.last_font_settings = dict()
        self.current_font = StringVar()
        self.receive_last_font()

    def receive_last_font(self):
        settings = {'font': None}
        read_start_parameters_from_db(settings, 'last')
        if settings['font']:
            self.current_font.set(str(settings['font']))
        else:
            self.current_font.set('Arial')
        self.last_font_settings = settings

    def save_last_font(self):
        win_settings = {'font': self.current_font.get()}
        for key in self.last_font_settings:
            if self.last_font_settings[key] == win_settings[key]:
                del win_settings[key]
        if win_settings:
            write_exit_parameters_in_db(win_settings, 'last')
            print(win_settings)