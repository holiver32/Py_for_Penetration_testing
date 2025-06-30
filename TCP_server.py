import socket

#Creating the socket
serversocket - socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

#Binding to socket
seversocket.bind(('192.168.178.24', port)) #Host will be replaced/substitued with IP, if changed and not running on host.

#Starting TCP listener
seversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = seversocket.accept()

    print("received connection from %s " % str(address))

    message = 'hello! thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()