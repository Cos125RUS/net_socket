import socket
import threading

nickname = input("Enter nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('45.12.237.90', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(f'\033[34m{message}\033[0m')
        except:
            print("Connection error")
            client.close()
            break


def write():
    while True:
        try:
            message = f'\033[35m{nickname}: \033[36m{input()} \033[0m'
            client.send(message.encode('ascii'))
        except:
            print('\033[31m   Writen error \033[0m')


receive_thread = threading.Thread(target=receive).start()
write_thread = threading.Thread(target=write).start()
