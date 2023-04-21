from tkinter import Menu


class ViewSubMenu(Menu):

    def __init__(self, parent, wind):
        super().__init__(parent)
        self.config(tearoff=False)
        self.add_radiobutton(label='Темная',
                             value='dark',
                             variable=wind.note_text.current_window_theme,
                             command=wind.note_text.change_theme)
        self.add_radiobutton(label='Светлая',
                             value='light',
                             variable=wind.note_text.current_window_theme,
                             command=wind.note_text.change_theme)
