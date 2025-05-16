import socket

HOST = '127.0.0.1'  # Server IP address (localhost)
PORT = 65432        # Port to connect to (same as server)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to server

    while True:
        message = input("Enter message (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        s.sendall(message.encode())       # Send message
        data = s.recv(1024)               # Receive echo

        print("Echo from server:", data.decode())
