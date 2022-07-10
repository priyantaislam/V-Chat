import socket
import threading

HOST = '127.0.0.1'
PORT = 6666

server = server.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

clients = []
usernames = []

#broadcast
def broadcast(message):
        for client in clients:
                client.send(message)

#handle
def handle(client):
        while True:
                try:
                        message = client.recv(1024)
                        print(f"{nicknames[clients.index(client)]} says {message}")
                        broadcast(message)

                except:
                        index = clients.index(client)
                        clients.remove(client)
                        client.close()
                        uname = usernames[index]
                        usernames.remove(uname)


#receive
def receive():
        while True:
                client, address = server.accept()
                print(f"Connected with {str(address)}!\n")
        
        client.send("USRN".encode('utf-8'))
        uname = client.recv(1024)
        
        nicknames.append(uname)
        clients.append(client)

        print(f"Username of the client is {uname}!\n")
        broadcast(f"{uname} just joined the chat!\n".encode('utf-8'))
        client.send("Connected to the server!\n".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server running . . .")
receive()