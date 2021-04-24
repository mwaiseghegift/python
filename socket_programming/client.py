import socket

HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
disconnect_alert_message = "disconnected"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect()