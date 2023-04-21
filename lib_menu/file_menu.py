from tkinter import Menu


class FileMenu(Menu):

    def __init__(self, wind):
        super().__init__(wind)
        self.config(tearoff=False)
        self.add_command(label='Открыть...', command=wind.note_text.loading_text)
        self.add_command(label='Сохранить как...', command=wind.note_text.save_text)
        self.add_separator()
        self.add_command(label='Закрыть', command=wind.window_exit)
