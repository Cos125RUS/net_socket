import time
from tkinter import *
from tkinter import messagebox

from connector import *


class UI:
    def __init__(self):
        self.connect = Connector(self)
        self.window = Tk()
        self.window['bg'] = '#fafafa'
        self.window.title('Massager')
        self.window.geometry('640x400')
        self.window.iconbitmap(default='icon.ico')
        self.window.resizable(width=False, height=False)
        self.entry_text = Entry(width=50, font=('Courier', 12))
        self.entry_text.place(x=20, y=370)
        self.enter_button = Button(self.window, text='Отправить', width=10, height=1,
                                   font=('Courier', 8), command=self.enter)
        self.enter_button.place(x=540, y=368)
        self.canvas = Canvas(self.window, height=340, width=610)
        self.canvas.place(x=10, y=10)
        # self.chat_field = Frame(self.canvas, relief=RAISED, borderwidth=0)
        # self.chat_field.pack(fill=NONE, expand=False, side=LEFT, padx=5, pady=5, )
        # self.chat_field.place(relheight=1, relwidth=1)
        self.count_line = 1
        self.scroll = Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.scroll.place(x=595, relheight=1)
        self.canvas.config(yscrollcommand=self.scroll.set)

    def start(self):
        self.connect.connect('Valerii')
        self.window.mainloop()

    def view(self, message):
        Label(self.canvas, text=message, borderwidth=0, font=10).place(x=5,
                    y=self.count_line*25-15, relx=0.01, rely=0.01)
        self.count_line += 1

    def enter(self):
        value = self.entry_text.get()
        if value != '':
            self.connect.write(value)
            time.sleep(0.1)
            self.entry_text.delete(0, 'end')
