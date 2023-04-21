from tkinter import Menu


class FontSubMenu(Menu):
    def __init__(self, parent, wind):
        super().__init__(parent)
        self.config(tearoff=False)
        self.add_radiobutton(label='Arial',
                             value='Arial',
                             font=('Arial', 10, 'normal'),
                             variable=wind.note_text.current_font,
                             command=wind.note_text.change_font)
        self.add_radiobutton(label='Comic Sans MS',
                             value='Comic Sans MS',
                             font=('Comic Sans MS', 10, 'normal'),
                             variable=wind.note_text.current_font,
                             command=wind.note_text.change_font)
        self.add_radiobutton(label='Times New Roman',
                             value='Times New Roman',
                             font=('Times New Roman', 10, 'normal'),
                             variable=wind.note_text.current_font,
                             command=wind.note_text.change_font)
