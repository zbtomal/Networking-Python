import socket

HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 65432        # Port to connect to

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

print("Current Date & Time from Server:", data.decode())
