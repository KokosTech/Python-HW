import socket
import threading
from datetime import datetime

import aqi
import pyowm

# Weather

APIKEY = 'b7ef9a1647a36bdb99c857407dc5e116'
OpenWMap = pyowm.OWM(APIKEY)
mgr = OpenWMap.weather_manager()
Weather = mgr.weather_at_place("Sofia")
Data = Weather.weather

# Server

HEADER = 64
PORT = 50007
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "dis"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                print(f"[DISCONNECTING] {addr}")
                connected = False
                break

            print(f"[{addr}] {msg}\n")
            if msg.lower() == "weather":
                conn.send(f"The temperature today will be: {Data.temperature('celsius')['temp']}C".encode(FORMAT))
            elif msg.lower() == "time":
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                conn.send(f"The time right now is: {current_time}".encode(FORMAT))
            elif msg.lower() == "air quality":
                myaqi = aqi.to_iaqi(aqi.POLLUTANT_PM25, '12', algo=aqi.ALGO_EPA)
                conn.send(f"The AQI (Air Quality Index) is: {myaqi}IAQI".encode(FORMAT))
            else:
                conn.send(f"The command doesn't exist, please try again!".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting")
start()
