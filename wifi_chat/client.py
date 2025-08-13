import socket
import threading
import sys

HOST = '192.168.63.61'  # Replace with your server's IP address
PORT = 65432

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                print("[Server disconnected]")
                break
            print(f"\rFriend: {message.decode()}\n> ", end='')
        except:
            print("[Error receiving message]")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except Exception as e:
        print(f"[Connection failed] {e}")
        sys.exit(1)
    print("Connected to the chat server. Type messages below (type 'exit' to quit):")
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    while True:
        message = input('> ')
        if message.lower() == 'exit':
            break
        try:
            client.sendall(message.encode())
        except:
            print("[Error sending message]")
            break
    client.close()

if __name__ == "__main__":
    main()
