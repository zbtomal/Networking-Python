import socket
import threading

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432

clients = []

# Broadcast message to all clients except the sender
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.sendall(message)
            except:
                pass

def handle_client(client, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            print(f"{addr}: {message.decode()}")
            broadcast(message, client)
        except:
            break
    print(f"[DISCONNECT] {addr} disconnected.")
    clients.remove(client)
    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    main()
