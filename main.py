import socket
import threading

host = 'localhost'
port = 55555

clients = []
nicknames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index()
            clients.remove(client)
            client.close()
            nick_ = nicknames[index]
            broadcast(f"{nick_} left the chat".encode('ascii'))
            nicknames.remove(nick_)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send("Hit Enter to join chat ".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        clients.append(client)
        nicknames.append(nickname)

        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send("connected to server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print("Server is listening....")
receive()
