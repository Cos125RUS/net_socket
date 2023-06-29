#!/bin/python3

import socket
import threading
from user import *

host = '45.12.237.90'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

users = []


def broadcast(message):
    for user in users:
        user.client.send(message)


def handle(user):
    while True:
        try:
            broadcast(user.client.recv(1024))
        except:
            user.client.close()
            broadcast(f'{user.nickname.encode("ascii")} left!')
            users.remove(user)
            break


def receive():
    while True:
        client, address = server.accept()
        client.send('NICK'.encode('ascii'))
        user = User(f'{client.recv(1024).decode("ascii")}', client, f'{address[0]}:{str(address[1])}')

        log_message = f"Connected with {user.address} Nickname is {user.nickname}"
        print(log_message)
        with open('log.txt', 'a') as log:
            log.write(f'{log_message}\n')

        client.send('Connected to server!'.encode('ascii'))
        broadcast(f"{user.nickname} joined!".encode('ascii'))
        users.append(user)

        threading.Thread(target=handle, args=(user,)).start()


print("Server if listening...")
receive()
