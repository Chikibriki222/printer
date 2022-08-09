from tkinter import *
import os
import time

path = './files'
i_files = os.listdir(path)


def clicked():
    for file in i_files:
        file_path = f'{path}\\{file}'

        if os.path.isfile(file_path):
            try:
                os.startfile(file_path, 'print')
                print(f'Печатается {file}')

                time.sleep(5)
            except:
                print(f'Внимание: {file} не удалось распечатать!')


window = Tk()
window.title('Принтер двухсторонних документов')
window.geometry('400x250')

lbl = Label(window, text='Нажми на кнопку для печати')
lbl.grid(column=4, row=0)

btn = Button(window, text='Печатать', command=clicked)
btn.grid(column=4, row=5)

window.mainloop()