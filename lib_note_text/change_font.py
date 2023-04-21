from lib_note_text.choice_font import ChoiceFont


class ChangeFont(ChoiceFont):
    def __init__(self):
        super().__init__()
        self.change_font()

    def change_font(self):
        self.config(font=self.font_view[self.current_font.get()]['font'])
