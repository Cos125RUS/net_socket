import time
from tkinter import *
from connector import *


class UI:
    def __init__(self, login_name):
        self.login_name = login_name
        self.connect = Connector(self)
        self.window = Tk()
        self.window.title('Messager')
        self.window.geometry('640x400')
        self.window.iconbitmap(default='icon.ico')
        self.window.resizable(width=False, height=False)
        self.entry_text = Entry(width=50, font=('Courier', 12))
        self.entry_text.place(x=20, y=370)
        self.entry_text.bind("<KeyPress-Return>", self.entered)
        self.enter_button = Button(self.window, text='Отправить', width=10, height=1,
                                   font=('Courier', 8), command=self.enter)
        self.enter_button.place(x=540, y=368)
        self.frame = Frame(self.window, height=340, width=610)
        self.frame.place(x=10, y=10)
        self.message_field = Listbox(self.frame, font=10, selectbackground='grey')
        self.message_field.place(relheight=1, relwidth=1)
        self.scrollbar = Scrollbar(self.message_field)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def start(self):
        self.connect.connect(self.login_name)
        self.window.mainloop()

    def view(self, message):
        lines = []
        line_size = 60
        if len(message) > line_size:
            while len(message) > line_size:
                if message[:line_size].count(' '):
                    string = message[:line_size].rsplit(" ", 1)
                    lines.append(string[0])
                    message = string[1] + message[line_size:]
                else:
                    lines.append(message[:line_size])
                    message = message[line_size:]
        lines.append(message)
        for line in lines:
            self.message_field.insert(END, f" {line}")
            self.message_field.yview(END)


    def enter(self):
        value = self.entry_text.get()
        if value != '':
            self.connect.write(value)
            time.sleep(0.1)
            self.entry_text.delete(0, 'end')

    def entered(self, event):
        self.enter()
