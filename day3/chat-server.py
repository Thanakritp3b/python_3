import socket
import threading

clients = []



def boardcast(message, sender_conn = None):
    for client in clients:
        if client != sender_conn:
            try:
                client.send((message+"\n").encode())
            except:
                clients.remove(client)

def handle_client(conn, addr):
    print(f"New client connect from {addr}")
    message_received = ""
    while True:
        try:
            while True:
                data = conn.recv(32)
                if data:
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    print(f"Connection lost from {addr}")
                    clients.remove(conn)
                    conn.close()
                    return
            if message_received:
                print(f"\n Received message:{message_received}")
                messsage_from_client = f"Client {addr}: {message_received}"
                boardcast((messsage_from_client), conn)
                message_received = ""
        except:
            print(f"Connection lost from {addr}")
            clients.remove(conn)
            conn.close()
            return
        
def send_server_message():
    while True:
        message = input("Enter a message to broadcast to all clients: ")
        if message.lower() == "exit":
            break
        print(f"Broadcasting message: {message}")
        boardcast_message = f"Server: {message}"
        boardcast(boardcast_message, None)
        print("Message broadcasted")

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

t1 = threading.Thread(target=send_server_message)
t1.daemon = True
t1.start()

while True:
    try:
        conn, addr = s.accept()
        clients.append(conn)
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.daemon = True
        t.start()
    except KeyboardInterrupt:
        print("disconnecting clients")
        break

for c in clients:
    c.close()
if s:
    s.close()
print("Server finished")