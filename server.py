#!/usr/bin/python

import socket 
import sys
import threading

server_Port = 80
server_Ip = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((server_Ip, server_Port))
server.listen(5)


try:
    conn, addr = server.accept()
    print("Connected", addr)
    while True:
        msg = conn.recv(1024).decode()
        print(msg)

        if msg == "":
            print(f"Exiting Programme")
            break
        server.close

except KeyboardInterrupt:
    print("Exiting Programme")
    server.close
