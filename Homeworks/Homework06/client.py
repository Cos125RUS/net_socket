import socket
import threading

nickname = input("Введите имя пользователя: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('45.12.237.90', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(f'\033[34m{message}\033[0m')
        except:
            print("Ошибка соединения")
            client.close()
            break


def write():
    while True:
        try:
            message = f'\033[35m{nickname}: \033[36m{input()} \033[0m'
            client.send(message.encode('utf-8'))
        except:
            print('\033[31m  Ошибка ввода \033[0m')


threading.Thread(target=receive).start()
threading.Thread(target=write).start()
