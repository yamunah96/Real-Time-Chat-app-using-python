import socket

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind server
server.bind(("127.0.0.1", 5555))

# start listening
server.listen()

print("Server is running...")

client, address = server.accept()

print("Connected with", address)

while True:
    message = client.recv(1024)
    print("Client:", message.decode())