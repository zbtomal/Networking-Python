import socket
import threading
HOST = '192.168.63.157'
PORT = 65432

def receive_messages(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("\n"+data.decode()+"\n>")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()
    
    while True:
        msg = input("Enter msg: >")
        s.sendall(msg.encode())