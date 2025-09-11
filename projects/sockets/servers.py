import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))


server.listen(5)
print('server listing on port neinneinneinnein')

while True:
    client, addr = server.accept()
    print(f'connection frm {addr}')
    print(client.recv(1024).decode())
    client.send('ayoh WAZZ UP CLIENT'.encode())
    # client.close()
#     break
# server.close()