import socket
import threading


def send_message(s):
    while True:
        message = input("Enter a message if you want to exit, type 'exit': ")
        if message.lower() == "exit":
            s.close()
            break
        s.send((message+"\n").encode())
        print("Message sent ")

def receive_message(s):
    while True:
        try :
            message_received = ""
            while True:
                data = s.recv(32)
                if data:
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    print("Connection lost!")
                    return
            if message_received:
                print("Received message: ", message_received)

        except:
            print("Connection lost!")
            return




HOST = '127.0.0.1'
PORT = 21002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    t1 = threading.Thread(target=send_message, args=(s,))
    t2 = threading.Thread(target=receive_message, args=(s,))

    t1.daemon = True
    t2.daemon = True

    t1.start()
    t2.start()
    
    t1.join()

print("Client finished")