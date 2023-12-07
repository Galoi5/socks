import socket
import threading
import os

clients = []
nicknames = []

def host():
    while True:
        os.system('cls||clear')
        print("Host server on ip address:\n")
        option = input("(1) localhost\n")
        if option == '1':
            host = "localhost"
            port = int(input("port: "))

            global server

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen()
            break
        
def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message) 

        except socket.error:
            if client in clients:
                index = clients.index(client)
                client.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the Chat!'.encode('ascii'))
                nicknames.remove(nickname)
                break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send('NICK'.encode('ascii'))
        pseudonym = client.recv(1024).decode('ascii')

        nicknames.append(pseudonym)
        clients.append(client)

        broadcast(f'{pseudonym} joined the Chat'.encode('ascii'))
        client.send('Connected to the Server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print('Server is Listening ...')
host()
receive()