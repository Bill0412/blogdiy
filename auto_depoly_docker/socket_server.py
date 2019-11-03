# References
# 1. Socket server:  https://realpython.com/python-sockets/

import socket
# import threading
server_addr = ("", 5000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(server_addr)
    server.listen()
    conn, addr = server.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            # if not data:
            #     break
            #     conn.sendall(data)
            print(data)




