import socket

HOST = '127.0.0.1'
PORT = 33939

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    i = ""
    while i != "exit":
        i = input("")
        s.sendall(bytes(i,'utf-8'))
        data = s.recv(1024)
        print('Received', repr(data))
