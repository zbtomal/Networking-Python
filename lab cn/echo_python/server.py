import socket
Host = '127.0.0.1'
Port = 65432
numbers = []

def handle_numbers(num):
    x = ""
    for i in num:
        if i.isdigit():
            x += i
        else:
            if x:
                num_app(x)
                x = ""

def num_app(num):
    x = 0
    n = len(num)
    i = 0
    while i < n:
        x += (int(num[i])) * pw(n-i)
        i += 1
    numbers.append(x)

def pw(num):
    x = 1
    i = 1
    while i < num:
        x *= 10
        i += 1
    return x

def sendans(conn):
    numbers.sort()
    ans = ""
    n = len(numbers)
    total = 0
    ans+=f"Min : {numbers[0]}\n"
    ans+=f"Max : {numbers[n-1]}\n"
    ans+=f"Numbers: "
    
    for i in numbers:
        total+=i
        ans += " "
        ans += str(i)

    avg = total/n
    ans+=f"\nAvg: {avg}\n"
    conn.sendall(ans.encode())
    numbers.clear()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen()

    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        msg = data.decode()
        print("Recieved: ", msg)

        handle_numbers(msg)
        sendans(conn)