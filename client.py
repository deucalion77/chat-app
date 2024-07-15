import socket

client_Port = 80
client_Ip = '127.0.0.1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((client_Ip, client_Port))

try:
    while True:
        data = input("user Input: ")
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