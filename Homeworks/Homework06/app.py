from ui import *
from login import Login

class App:
    def __init__(self):
        self.chat_window = None
        self.login_window = None
        self.login_name = ''

    def start(self):
        self.login_window = Login()
        self.login_name = self.login_window.get_login()
        self.chat_window = UI(self.login_name).start()
