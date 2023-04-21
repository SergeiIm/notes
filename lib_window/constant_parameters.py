from lib_window.receive_save_geometry import WindGeometry


class ConstantsWin(WindGeometry):
    w_title = "Заметки"
    w_name_icon = 'images/icon.ico'

    def __init__(self):
        super().__init__()
        self.title(self.w_title)
        self.iconbitmap(self.w_name_icon)

