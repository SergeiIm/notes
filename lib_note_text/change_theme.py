from lib_note_text.choice_theme import ChoiceTheme


class ChangeTheme(ChoiceTheme):

    def __init__(self):
        super().__init__()
        self.change_theme()

    def change_theme(self):
        name_theme = self.current_window_theme.get()
        self.config(bg=self.theme_view[name_theme]['text_bg'])
        self.config(fg=self.theme_view[name_theme]['text_fg'])
        self.config(insertbackground=self.theme_view[name_theme]['insert_bg'])
        self.config(selectbackground=self.theme_view[name_theme]['select_bg'])
