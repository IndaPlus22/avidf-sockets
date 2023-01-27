
import socket
import threading


host = '127.0.0.1'
port = 55555

# Start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Listens for clients
clients = []
usernames = []

 
# Broadcast to connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

#Message handling
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # removing left clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast('{} left!'.format(username).encode('ascii'))
            usernames.remove(username)
            break

# Listen for clients
def receive():
    while True:
        
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # get username
        client.send('NICK'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        # print and broadcast
        print("username is {}".format(username))
        broadcast("{} joined!".format(username).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # threads
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()