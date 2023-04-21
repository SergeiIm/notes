from tkinter import Tk
from lib_metods.working_with_db import read_start_parameters_from_db, write_exit_parameters_in_db


class WindGeometry(Tk):

    w_geometry = '600x400+100+100'
    w_state = 'normal'
    w_resizable_x = True
    w_resizable_y = True

    def __init__(self):
        super().__init__()
        self.last_settings = dict()
        self.receive_last_geometry()
        self.geometry(self.w_geometry)
        self.minsize(320, 200)
        self.state(self.w_state)
        self.resizable(self.w_resizable_x, self.w_resizable_y)

    def receive_last_geometry(self):
        settings = {'geometry': None, 'state': None}
        read_start_parameters_from_db(settings, 'last')
        if settings['geometry'] and settings['state']:
            self.w_geometry = settings['geometry']
            self.w_state = settings['state']
            self.last_settings = settings

    def save_last_geometry(self):
        win_settings = {'geometry': self.geometry(), 'state': self.state()}
        for key in self.last_settings:
            if win_settings[key] == self.last_settings[key]:
                del win_settings[key]
        if win_settings:
            write_exit_parameters_in_db(win_settings, 'last')
            print(win_settings)

