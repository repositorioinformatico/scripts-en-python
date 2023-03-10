# server.py
import socket                   # Import socket module
port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
#creates the file we'll send
with open('mytext.txt', 'w') as f:
    f.write('mytext file content')
print('Server listening....')
while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
    print('Done sending')
    message='Thank you for connecting'
    conn.send(message.encode('utf-8'))
    #conn.send('Thank you for connecting')
    conn.close()
