import socket

host = input(str("Enter Server IP: "))
port = 9999

with socket.socket() as c:
    c.connect((host, port))
    print(f"Connected to {host}")

    name = input(str("Enter Your Name: "))
    c.send(name.encode())

    message = c.recv(1024)
    print(message.decode())

    while True:
        message = c.recv(1024).decode()
        print(f"host > {message}")
        message = input(str("Me > "))
        if message == "bye":
            break
        c.send(message.encode())

        # new = input(str("> "))
        # c.send(new.encode())
