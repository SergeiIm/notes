from tkinter import Menu
from lib_metods.up_windows import show_wind_about_authors


class HelpMenu(Menu):
    def __init__(self):
        super().__init__()
        self.config(tearoff=False)
        self.add_command(label='О авторах...', command=show_wind_about_authors)
