import socket
import threading
import sys

clients = []
address = []
address_to_conn = {}


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
            if message_received.lower() == "exit\n":
                print(f"Client {addr} has disconnected")
                clients.remove(conn)
                conn.close()
                return

            if message_received.startswith("private"):
                private_message(conn, addr, message_received)
                message_received = ""
                continue
                
            if message_received:
                print(f"Received message:{message_received}")
                messsage_from_client = f"Client {addr}: {message_received}"
                boardcast((messsage_from_client), conn)
                message_received = ""
        except:
            print(f"Connection lost from {addr}")
            clients.remove(conn)
            conn.close()
            return
def private_message(conn, addr, message):
    print(f"Private message received from {addr}")
    parts = message.strip().split("-", 2)
    if len(parts) < 3:
        conn.send("Invalid private message command. Use: private-<receiver>-<message>\n".encode())
        return
    receiver = parts[1].strip()
    msg_content = parts[2].strip()
    
    receiver_conn = None
    for client_addr, client_conn in address_to_conn.items():
        if str(client_addr) == receiver: 
            receiver_conn = client_conn
            break
    
    if not receiver_conn:
        conn.send(f"Receiver {receiver} not found\n".encode())
        return
    
    try:
        receiver_conn.send(f"Private message from {addr}: {msg_content}\n".encode())
        conn.send(f"Private message sent to {receiver}\n".encode())
    except:
        conn.send("Error sending private message\n".encode())

    

        
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
        address.append(addr)
        address_to_conn[addr] = conn
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