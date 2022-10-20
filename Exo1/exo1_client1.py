from socket import *
from time import *

serverName = '127.0.0.1'
serverPort = 3000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

nbReq = 2
i = 0
while i < nbReq:
    message= "hello !!" + str(i+1)
    clientSocket.send(message.encode("utf-8"))
    modifiedMessage = clientSocket.recv(2048)
    print(modifiedMessage.decode("utf-8"))
    i += 1

clientSocket.close()
