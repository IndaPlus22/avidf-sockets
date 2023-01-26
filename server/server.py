import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to address
s.bind(("127.0.0.1", 1234))

# Listen connections
s.listen()

# Keep track clients in a dictionary
clients = {}

while True:
    # Accept a connection
    c, addr = s.accept()
    print("Connection from: " + str(addr))

    # username
    username = c.recv(1024).decode()
    print("Username: " + username)

    # Add the client to the dictionary
    clients[c] = username

    # Send a message to connected clients
    for client in clients:
        client.send(bytes("{} has joined the chat.".format(username)))

    # Receive messages
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("Received from {}: {}".format(username, data.decode()))
        for client in clients:
            client.send(bytes("{}: {}".format(username, data.decode()), "utf-8"))

    # Remove the client from the dictionary
    del clients[c]

    # Send a message to all connected clients
    for client in clients:
        client.send(bytes("{} has left the chat.".format(username)))