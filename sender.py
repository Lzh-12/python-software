import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("8.138.172.67", 8689))

while True:
    data = input("Enter: ")
    client.send(data.encode("utf-8"))
