import socket
HOST = '127.0.0.1'
PORT = 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    #s.sendall(b'bye')
    data = s.recv(1024)
print('Devolviendo como un eco lo siguiente: ', repr(data))
