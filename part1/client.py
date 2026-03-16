import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",5555))

while True:
    message = input("You: ")
    client.send(message.encode())