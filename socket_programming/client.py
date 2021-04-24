import socket

HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
disconnect_alert_message = "disconnected"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def send_message(the_message):
    message = the_message.encode('utf-8')
    message_length = len(message)
    send_length = str(message_length).encode('utf-8')
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode("utf-8"))
    
send_message("Hello Gift")
input()
send_message("Save us master")
input()
send_message(disconnect_alert_message)