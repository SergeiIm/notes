from tkinter import Menu
from lib_menu.option_view_menu import ViewSubMenu
from lib_menu.option_font_menu import FontSubMenu


class OptionMenu(Menu):
    def __init__(self, wind):
        super().__init__(wind)

        self.config(tearoff=False)
        # Вид
        view_menu = Menu(self, tearoff=0)
        view_menu_sub = ViewSubMenu(view_menu, wind)
        self.add_cascade(label='Тема...', menu=view_menu_sub)

        # Шрифт
        font_menu = Menu(self, tearoff=0)
        font_menu_sub = FontSubMenu(font_menu, wind)
        self.add_cascade(label='Шрифт...', menu=font_menu_sub)
