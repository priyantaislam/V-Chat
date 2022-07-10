import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 9999

class Client:

        def __init__(self,host,port):

                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((host,port))

                msg = tkinter.TK()
                msg.withdraw()

                self.uname = simpledialog.askstring("Username", "Please choose a username", parent=msg)
                
                self.gui_done = False
                self.running = True

                gui_thread = threading.Thread(target=self.gui_loop)
                recv_thread = threading.Thread(target=self.receive)

                gui_thread.start()
                recv_thread.start()

        def gui_loop(self):
                self.win = tkinter.TK()
                self.win.configure(bg="lightgray")
                
                self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
                self.chat_label.config(font=("Arial",12))
                self.chat_label.pack(padx=20,pady=5)

                self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
                self.text_area.pack(padx=20,pady=5)
                self.text_area.config(state='disabled')

                

        

        def receive(self):
                pass