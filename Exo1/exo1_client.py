from socket import *
from time import *

serverName = '127.0.0.1'
serverPort = 4050

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

message= "hello ???"
clientSocket.send(message.encode("utf-8"))


modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode("utf-8"))

clientSocket.close()
