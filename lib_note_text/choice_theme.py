from lib_note_text.read_and_write_text_from_file import ReadWrite
from lib_metods.working_with_db import read_start_parameters_from_db, write_exit_parameters_in_db
from tkinter import StringVar


class ChoiceTheme(ReadWrite):
    theme_view = {'dark': {'text_bg': 'black', 'text_fg': 'grey', 'insert_bg': 'white', 'select_bg': '#8D917A'},
                  'light': {'text_bg': 'white', 'text_fg': 'black', 'insert_bg': 'brown', 'select_bg': 'grey'}}

    def __init__(self):
        super().__init__()
        self.last_theme_settings = dict()
        self.current_window_theme = StringVar()
        self.receive_last_theme()

    def receive_last_theme(self):
        settings = {'theme': None}
        read_start_parameters_from_db(settings, 'last')
        if settings['theme']:
            self.current_window_theme.set(str(settings['theme']))
        else:
            self.current_window_theme.set('light')
        self.last_theme_settings = settings

    def save_last_theme(self):
        win_settings = {'theme': self.current_window_theme.get()}
        for key in self.last_theme_settings:
            if self.last_theme_settings[key] == win_settings[key]:
                del win_settings[key]
        if win_settings:
            write_exit_parameters_in_db(win_settings, 'last')
            print(win_settings)
