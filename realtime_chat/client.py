import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receive_messages():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print("\n" + data.decode() + "\n> ", end="")
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input("> ")
    client.sendall(msg.encode())
