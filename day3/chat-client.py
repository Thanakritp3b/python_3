import socket
import threading
import sys


def send_message(s):
    while True:
        message = input("Enter a message if you want to exit, type 'exit': ")
        if message == "exit":
            flag[0] = True
            s.close()
            break
        s.send((message+"\n").encode())
        print("Message sent ")
            




HOST = '127.0.0.1'
PORT = 21002
flag = [False]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    t1 = threading.Thread(target=send_message, args=(s,))
    t1.start()

    while flag[0] == False:
        message_received = ""
        while True:
            data = s.recv(32)
            if data:
                message_received += data.decode()
                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                flag[0] = True
                break
        if not message_received:
            break
        if message_received:
            print("\n"+ "Received message: ", message_received)

print("Client finished")