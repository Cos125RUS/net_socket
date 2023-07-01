from tkinter import *

class Login:
    def __init__(self):
        self.login_name = ''
        self.window = Tk()
        self.window.title('Massager')
        self.window.geometry('350x200')
        self.window.iconbitmap(default='icon.ico')
        self.window.resizable(width=False, height=False)
        Label(text="Введите логин", pady=30, font=12).pack(side=TOP)
        self.login_field = Entry(width=20, font=('Courier', 12))
        self.login_field.pack(side="top")
        self.login_field.bind("<KeyPress-Return>", self.entered)
        Button(text="Подтвердить", font=12, command=self.enter).pack(side=TOP, pady=30)
        self.window.mainloop()

    def enter(self):
        self.login_name = self.login_field.get()
        self.window.destroy()

    def get_login(self):
        return self.login_name

    def entered(self, event):
        self.enter()
