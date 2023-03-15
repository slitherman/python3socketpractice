import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTED"
SERVER = "192.168.0.199"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    messsage = msg.encode(FORMAT)
    msg_length = len(messsage)
    send_length= str(msg_length).encode(FORMAT)
    send_length += b'' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(messsage)
    print(client.recv(2048).decode((FORMAT)))
    send("hello world")
    input()
    send("hello everyone")
    input()
    send("hello matheu")
    send(DISCONNECT_MESSAGE)



