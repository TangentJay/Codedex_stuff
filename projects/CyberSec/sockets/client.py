import socket

msg =input('send something: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1',9999))  

client.send(msg.encode())
print(client.recv(1024).decode())

