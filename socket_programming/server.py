import socket
import threading

HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
disconnect_alert_message = "disconnected"

#create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def handle_client(connection, address):
    print(f"New Connection {address} just connected")
    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode("utf-8")
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode("utf-8")
            
            if message == disconnect_alert_message:
                connected = False
            
            print(f"{address} - {message}")
            connection.send("Message Received".encode("utf-8"))
    connection.close()

def start():
    server.listen()
    print(f"Server Listening to port {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")

print("server starting")
start()