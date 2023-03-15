import socket
import threading

# the first msg to the server from the client is going to be a 64bit header
HEADER = 64
Port = 5050
# grabs ip from hostname
SERVER = socket.gethostbyname(socket.gethostname())
# when you bind a socket to an address it needs to be in a tuple with the server and port
ADDR = (SERVER, Port)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTED"
# creates socket and picks a familu and type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket has bound to the address
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    # this  line of code blocks itself until it receives a message which is why it must be threaded
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"{addr} {msg}")
        conn.send(" Msg recieved".encode(FORMAT))

        conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on :{server}")
    while True:
        # the line waits for a new connection to the server, and then it stores the address of the connection
        # eg the port and ip address and then it will store an object that will allow us to send info to the connection
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} - ")


print("[STARTING] the server is starting...")
start()
