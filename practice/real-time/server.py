import socket
import threading

HOST = '0.0.0.0'
PORT = 65432
clients=[]

def handle_client(conn):
    addr = conn.getpeername()
    print(f"Connected by: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = f"[Port {addr[1]}]: {data.decode()}".encode()
        for client in clients:
            if client != conn:
                client.sendall(msg)
    print(f"{addr} Disconnted")
    clients.remove(conn)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
