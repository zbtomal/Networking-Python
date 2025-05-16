import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a socket (IPv4, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))         # Bind the socket to address
    s.listen()                   # Listen for incoming connections
    print(f"Server is listening on {HOST}:{PORT}")

    conn, addr = s.accept()      # Accept a connection
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)     # Receive data from client
            if not data:
                break
            print("Received:", data.decode())
            conn.sendall(data)         # Echo the data back
