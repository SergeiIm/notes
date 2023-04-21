from tkinter import Menu
from lib_menu.file_menu import FileMenu
from lib_menu.option_menu import OptionMenu
from lib_menu.help_menu import HelpMenu


class MenuObj(Menu):

    def __init__(self, parent):
        super().__init__(parent)

        file_menu = FileMenu(parent)
        self.add_cascade(label='Файл', menu=file_menu)

        option_menu = OptionMenu(parent)
        self.add_cascade(label='Настройки', menu=option_menu)

        help_menu = HelpMenu()
        self.add_cascade(label='Справка...', menu=help_menu)
