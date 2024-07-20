#! /usr/bin/python

import socket 
import sys

server_Port = 80
server_Ip = "127.0.0.1"

def server():
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


def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_Ip, server_Port))

    try:
        while True:
            data = input("")
            client.send(data.encode())
            #print(data)

        msg = client.recv(1024).decode()
        if not msg:
                print("Exiting Programe")
                #break
                conn.close()
            
        print(f"Received ", msg)
        client.close

    except KeyboardInterrupt:
        print("Exiting Programe")
        client.close

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <function>")
        sys.exit(1)
    
    function_name = sys.argv[1]
    
    if function_name == "-server":
        server()
    elif function_name == "-client":
        client()
    else:
        print(f"Unknown function '{function_name}'. Available functions: A, B")
        sys.exit(1)

