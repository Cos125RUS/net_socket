from tkinter import *
from connector import *


class UI:
    def __init__(self):
        self.connect = Connector(self)
        self.window = Tk()
        self.window.title('Massager')
        self.window.geometry('640x400')
        self.window.iconbitmap(default='icon.ico')
        self.window.resizable(width=True, height=True)
        self.entry_text = Entry(width=50, font=('Courier', 12))
        self.entry_text.place(x=20, y=370)
        self.enter_button = Button(self.window, text='Отправить', width=10, height=1,
                                   font=('Courier', 8), command=self.enter)
        self.enter_button.place(x=540, y=368)
        self.chat_field = Frame(self.window, relief=RAISED, borderwidth=0)
        # self.chat_field.pack(fill=NONE, expand=False, side=LEFT, padx=5, pady=5, )
        self.chat_field.place(x=10, y=20, anchor='w')

    def start(self):
        self.connect.connect('Valerii')
        self.window.mainloop()

    def view(self, message):
        Label(self.chat_field, text=message, borderwidth=0).pack(side=TOP)

    def enter(self):
        # print(f'{self.entry_text.get()}')
        self.connect.write(self.entry_text.get())

# TEST
# ui = UI()
# ui.main_frame()
# ui.start()
