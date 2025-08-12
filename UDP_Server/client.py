import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("You: ")
    client_socket.sendto(msg.encode(), (SERVER_HOST, SERVER_PORT))

    data, _ = client_socket.recvfrom(1024)
    print(f"Server: {data.decode()}")
