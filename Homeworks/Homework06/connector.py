import socket
import threading

class Connector:
    def __init__(self, ui):
        self.ui = ui
        self.nickname = ''
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('45.12.237.90', 55555))
        self.receive_thread = threading.Thread(target=self.receive, daemon=True)
        self.receive_thread.start()

    def connect(self, nickname):
        self.nickname = nickname

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message != 'NICK':
                    self.ui.view(message)
                else:
                    self.client.send(self.nickname.encode('utf-8'))
            except:
                with open('log.txt', 'a') as log:
                    log.write(f'Ошибка соединения!\n')
                    self.client.close()
                break

    def write(self, message):
        try:
            self.client.send(f'{self.nickname}: {message}'.encode('utf-8'))
        except:
            with open('log.txt', 'a') as log:
                log.write(f'Ошибка ввода! message: {message}\n')
