from concurrent.futures import thread
import socket
import threading

username = input("Choose an username: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 6666))

def receive():
        while True:
                try:
                        message = client.recv(1024).decode('ascii')
                        if message == "USRN":
                                client.send(username.encode('ascii'))
                        else:
                                print(message)

                except:
                        print("Error")
                        client.close()
                        break

def write():
        while True:
                message = f'{username}: {input("")}'
                client.send(message.encode('ascii'))


recv_thread = threading.Thread(target=receive)
recv_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

