#!/bin/python3

import socket
import threading
from user import *

host = '45.12.237.90'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
users = []


# Sending Messages To All Connected Clients
def broadcast(message):
    for user in users:
        user.client.send(message)


# Handling Messages From Clients
def handle(user):
    while True:
        try:
            # Broadcasting Messages
            broadcast(user.client.recv(1024))
        except:
            # Removing And Closing Clients
            # index = clients.index(client)
            # clients.remove(client)
            user.client.close()
            # nickname = nicknames[index]
            broadcast(f'{user.nickname.encode("ascii")} left!')
            # nicknames.remove(nickname)
            users.remove(user)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        # print(f"Connected with {address[0]}:{str(address[1])} ", end='')

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        # nickname = client.recv(1024).decode('ascii')
        # nicknames.append(nickname)
        # clients.append(client)
        user = User(f'{client.recv(1024).decode("ascii")}', client, f'{address[0]}:{str(address[1])}')
        users.append(user)
        # users[nickname] = user

        # Print And Broadcast Nickname
        log_message = f"Connected with {user.address} Nickname is {user.nickname}"
        print(log_message)
        broadcast(f"{user.nickname} joined!".encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        with open('log.txt', 'a') as log:
            log.write(f'{log_message}\n')

        # Start Handling Thread For Client
        threading.Thread(target=handle, args=(user,)).start()


print("Server if listening...")
receive()
