import pickle
import socket

# ToDo Weather, Time, AirQuality, Non-Existing_Command


BUFFER = 1024
PORT = 8080
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "dis"
SERVER = "34.77.60.185"  # Change for different server
ADDR = (SERVER, PORT)


def client():
    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl.connect(ADDR)
    return cl


def send(msg, client):
    d_msg = pickle.dumps(msg)
    client.send(d_msg)

    data = client.recv(1024)
    d_data = pickle.loads(pickle.loads(data))

    if msg.lower() == "weather":
        print(f"The Weather is {d_data[0]['main']} ({d_data[0]['description']})")
    else:
        print(d_data)


while True:
    msg = input("Enter a message: ")
    send(msg, client())
