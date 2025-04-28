import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("8.138.172.67", 8689))

while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))
