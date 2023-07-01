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
    try:
        if len(users) > 0:
            for user in users:
                user.client.send(message)
    except:
        print('Error')


def handle(user):
    while True:
        try:
            broadcast(user.client.recv(1024))
        except:
            user.client.close()
            broadcast(f'{user.nickname.encode("utf-8")} left!')
            users.remove(user)
            break


def receive():
    while True:
        client, address = server.accept()
        try:
            client.send('NICK'.encode('utf-8'))
            user = User(f'{client.recv(1024).decode("utf-8")}', client, f'{address[0]}:{str(address[1])}')

            log_message = f"Connected with {user.address} Nickname is {user.nickname}"
            print(log_message)
            with open('logs/log.txt', 'a') as log:
                log.write(f'{log_message}\n')

            client.send('Connected to server!'.encode('utf-8'))
            broadcast(f"{user.nickname} joined!".encode('utf-8'))
            users.append(user)

            threading.Thread(target=handle, args=(user,)).start()
        except:
            print(f"Connection with {address} failed")


print("Server if listening...")
receive()