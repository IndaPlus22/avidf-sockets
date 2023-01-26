import socket

# Create a socket 
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
c.connect(("127.0.0.1", 1234))

# Send the client's username
username = input("Enter your username: ")
c.send(bytes(username, "utf-8"))

print(c.recv(1024).decode())

while True:
    # Receive messages from the server
    data = c.recv(1024)
    if not data:
        break
    print(data.decode())
    # Send messages cack to the server
    message = input("Enter your message: ")
    c.send(bytes(message, "utf-8"))

# Close the connection
c.close()