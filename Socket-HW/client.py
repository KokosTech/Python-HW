import socket


# ToDo Weather, Time, AirQuality, Non-Existing_Command


HEADER = 64
PORT = 50007
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "dis"
SERVER = "192.168.0.148"  # Change for different server
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
        print(client.recv(2048).decode(FORMAT))


connection = True
while True:
    if connection:
        msg = input("Enter a message: ")
        send(msg)
        if msg == DISCONNECT_MESSAGE:
            connection = False
    else:
        print("DISCONNECTED FROM SERVER")
        break


