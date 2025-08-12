import socket

HOST = "127.0.0.1"
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP Server running on {HOST}:{PORT}")

client_addr = None

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Client: {data.decode()}")
    client_addr = addr  # remember client address

    msg = input("You: ")
    server_socket.sendto(msg.encode(), client_addr)