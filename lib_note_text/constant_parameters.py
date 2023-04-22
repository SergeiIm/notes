from tkinter import Text


class ConstantsText(Text):

    def __init__(self):
        super().__init__()

        self.config(padx=10)
        self.config(pady=10)
        self.config(wrap='word')
        self.config(spacing3=10)
        self.config(width=30)
        self.config(relief='flat')
