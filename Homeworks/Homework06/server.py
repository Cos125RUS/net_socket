#!/bin/python3

import socket
import threading

host = '45.12.237.90'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = {}


def broadcast(message):
    for client in clients.values():
        client.send(message)


def handle(nickname):
    while True:
        try:
            message = clients[nickname].recv(1024)
            broadcast(message)
        except:
            clients.pop(nickname)
            clients[nickname].close()
            broadcast(f'{nickname.encode("ascii")} left!')


def receive():
    while True:
        client, address = server.accept()
        print(client)

        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        clients[nickname] = client

        print(f"Nickname is {nickname}")
        broadcast(f'{nickname.encode("ascii")} joined!')
        client.send('Connected to server!'.encode('ascii'))
        # threading.Thread(target=handle, args=(nickname,)).start()


print("Server if listening...")
receive()
