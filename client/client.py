
import socket
import threading

# username
username = input("Choose your username: ")

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# recieve from serverx
def receive():
    #while recieving
    while True:
        try:

            message = client.recv(1024).decode('ascii')
            if message == 'User':
                client.send(username.encode('ascii'))
            else:
                print(message)
        
        except:
            # close for exception
            print("An error occured!")
            client.close()
            break

# Send to server
def write():
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('ascii'))

# threads for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()