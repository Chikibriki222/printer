from tkinter import *
import os
import time
from tkinter import scrolledtext

path = './files'
i_files = os.listdir(path)


def clicked():
    counter = 0
    for file in i_files:
        file_path = f'{path}\\{file}'

        if os.path.isfile(file_path):
            try:
                while counter <= 4:
                    os.startfile(file_path, 'print')
                    txt.insert(INSERT, f'Печатается {file}\n')
                    time.sleep(5)
                    counter = counter+1
                counter = 0



            except:
                txt.insert(INSERT, f'Внимание: {file} не удалось распечатать!\n')



window = Tk()
window.title('Принтер двухсторонних документов')
window.geometry('800x600')

lbl = Label(window, text='Нажми на кнопку для печати', font=("monospace", 20),pady=10)
lbl.grid(column=0, row=0)

btn = Button(window, text='Печатать', command=clicked, fg="black",font=("monospace", 14), width=72, pady=20)
btn.grid(column=0, row=1)

txt = scrolledtext.ScrolledText(window, width=100, height=20)
txt.grid(column=0, row=2)



window.mainloop()