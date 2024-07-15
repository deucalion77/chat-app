import socket 
import sys
import threading

server_Port = 80
server_Ip = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((server_Ip, server_Port))
server.listen(5)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_Ip, server_Port))


def message():
    while True:
        conn, addr = server.accept()
        print("Connected: ", addr)
        msg1 = conn.recv(1024).decode()
        print(msg1)

        if msg1 == "":
            print(f"Exiting Programme")
            break
            server.close

def message2():
    while True:
        msg2 = input()
        msg2 = msg2.encode()
        client.send(msg2)

        if msg2	 == "":
            print(f"Exiting Programme")
            break
            client.close

print(f"Listing on {(server_Ip, server_Port)}")

try:
    while True:
        t1 = threading.Thread(target=message)
        t2 = threading.Thread(target=message2)
        t1.start()
        t2.start()

except KeyboardInterrupt:
    print("Exiting Programme")
    server.close