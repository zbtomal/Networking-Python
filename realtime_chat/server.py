import socket
import threading

HOST = '127.0.0.1'
PORT = 65432
clients = []

def handle_client(conn):
    addr = conn.getpeername()
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            # Prepend sender's port to the message
            message = f"[Port {addr[1]}] {data.decode()}".encode()
            broadcast(message, conn)
        except:
            break
    clients.remove(conn)
    conn.close()

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.sendall(message)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server started on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print(f"Connected by {addr}")
    threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
