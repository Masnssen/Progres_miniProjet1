"""
    Reste a faire :
        Essaie de trouver le cas ou sa marche pas , question 2 exo1
"""

from socket import *
from time import *

serverName = '127.0.0.1'
serverPort = 2020

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

message= "Hello how are you serveur"

clientSocket.send(message.encode("utf-8"))
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode("utf-8"))
clientSocket.close()
