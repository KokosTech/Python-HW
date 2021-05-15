import socket
import os

# GUI Libs

import tkinter as tk

# ToDo Weather, Time, AirQuality, Non-Existing_Command

HEADER = 64
PORT = 50007
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "dis"
SERVER = "127.0.1.1"  # Change for different server
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    msg = client.recv(2048).decode(FORMAT)
    msgl = tk.Label(text=msg)
    msgl.pack()

def discon():
    send('dis')
    window.destroy()


window = tk.Tk()
window.geometry("500x300")
window.title("Socket App")

label = tk.Label(text="Socket App")
label.pack()

get_msg = tk.Entry()
button = tk.Button(text='Send', command=lambda: send(get_msg.get()))
dis = tk.Button(text='Disconnect', command=lambda: discon())

get_msg.pack()
button.pack()
dis.pack()

entry = tk.Entry()
submit_button = tk.Button()
window.mainloop()