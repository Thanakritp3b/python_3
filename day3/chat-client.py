import socket

HOST = '127.0.0.1'
PORT = 21002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    while True:
        message = input("Enter a message if you want to exit, type 'exit': ")
        s.send((message+"\n").encode())
        print("Message sent waiting for response")
        if message == "exit":
            break

        message_received = ""
        while True:
            data = s.recv(32)
            if data:
                message_received += data.decode()
                if message_received.endswith("\n"):
                    #print("End of message received")
                    break
            else:
                print("Connection lost!")
                break
        if message_received:
            print("Received message: ", message_received)

print("Client finished")