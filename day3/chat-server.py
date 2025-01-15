import socket
import sys
from pyexpat.errors import messages

HOST = '0.0.0.0'
PORT = 21002
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)

conn, addr = s.accept()
with conn:
    while True:
        message_received = ""
        while True:
            data = conn.recv(32)
            if data:
                message_received += data.decode()
                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                break

        if message_received:
            print("Received message: ", message_received)
            message_send = input("Enter a message if you want to exit, type 'exit': ")
            if message_send == "exit":
                break
            conn.send((message_send + "\n").encode())
            print("Message sent waiting for response")

        else:
            break

s.close()
print("Server finished")