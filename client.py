import socket
import threading
import os

stop_thread = False

def conn():
    os.system('cls||clear')

    global ip
    global port
    global pseudonym
    global client

    ip = input("\n Server IP: ")
    port = int(input("\n Server Port: "))
    pseudonym = input("\n Chat lifetime pseudonym: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

def receive():
    while True:
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(pseudonym.encode('ascii'))
            else:
                print(message)

        except socket.error:
            print('Error Occured while Connecting')
            client.close()
            break

def send():
    while True:
        if stop_thread:
            break

        message = f'{pseudonym}: {input("")}'
        client.send(message.encode('ascii'))

conn()

receive_thread = threading.Thread(target=receive)
receive_thread.start()
send_thread = threading.Thread(target=send)
send_thread.start()