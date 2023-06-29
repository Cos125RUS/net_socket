from tkinter import *

class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Massager')
        self.window.geometry('640x400')
        self.window.iconbitmap(default='icon.ico')
        self.window.resizable(width=True, height=True)

    def start(self):
        self.frame()
        self.window.mainloop()

    def frame(self):
        entry_text = Entry(width=50, font=('Courier', 12))
        entry_text.place(x=20, y=370)
        enter_button = Button(self.window, text='Отправить', width=10, height=1, font=('Courier', 8),
                              command=self.command)
        enter_button.place(x=540, y=368)



    def command(self):
        pass


# TEST
UI().start()