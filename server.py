import socket
import threading

host = '127.0.0.1'
port = 6666

server = server.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients = []
nicknames = []

#broadcast
def broadcast(message):
        for client in clients:
                client.send(message)

#receive
def receive():
        while True:
                client, address = server.accept()
                print(f"{str(address)} just joined the chat!")

