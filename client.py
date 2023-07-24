import socket
import threading

nickname = input("Enter a nickname: ")

server = 'localhost'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "Nick":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error ocurred :(")
            client.close()
            break


def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))


receiving_thread = threading.Thread(target=receive)
receiving_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()

