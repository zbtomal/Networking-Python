import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

# Function to handle each client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"[DISCONNECTED] {addr} disconnected.")
                break
            print(f"[RECEIVED from {addr}]: {data.decode()}")
            conn.sendall(data)

# Main server logic
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
