import socket

HOST = '192.168.164.2'  # Replace with the IP address of the receiver
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('new.txt', 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.sendall(data)
