from socket import *
from time import *

serverPort = 7000
serverSocket = socket (AF_INET, SOCK_STREAM)
serverSocket.bind (('',serverPort))

serverSocket.listen(1)
connectionSocket, address = serverSocket.accept()
print ('Server Ready')
sleep(30)
while True:
    message = connectionSocket.recv(2048)
    modifiedMesage= message.decode("utf-8").upper()
    connectionSocket.sendall(modifiedMesage.encode("utf-8"))
    
connectionSocket.close()
