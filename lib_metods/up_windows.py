from tkinter import messagebox
from tkinter import filedialog


def show_wind_about_authors():
    messagebox.showinfo(title='О авторах.',
                        message='автор и разработчик: Сергей.\n'
                                'Sergei.work23@gmail.com\n\n'
                                '       Белград, Сербия.\n'
                                ' © кон.2022г - нач.2023г.')


def read_from_a_file():
    open_file = filedialog.askopenfilename(title='Выбор файла.',
                                           filetypes=(('Текстовые документы (*.txt)', '*.txt'),
                                                      ('Все файлы', '*.*')))
    result = None
    if open_file:
        with open(open_file, 'rt', encoding='utf-8') as file:
            result = file.read()
    return result


def writing_in_file(text_file):
    save_name_file = filedialog.asksaveasfilename(
        filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*'))) + '.txt'
    with open(save_name_file, 'w', encoding='utf-8') as file:
        file.write(text_file)
