from lib_window.create_windows import CreateWindow
from tkinter import messagebox


class CloseWindow(CreateWindow):
    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.window_exit)

    def window_exit(self):
        answer = messagebox.askokcancel('Выход', 'Вы действительно хотите выйти?')
        if answer:
            self.window_menu.destroy()
            self.save_last_geometry()
            self.note_text.save_last_theme()
            self.note_text.save_last_font()
            self.destroy()
