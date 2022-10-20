from socket import *
from time import *
from threading import *
import os
clientPort_listening = 4050

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort_listening))
clientSocket.listen(1)

serverName = '127.0.0.1'
serverPort = 9080

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.connect((serverName,serverPort))

print ('Relayer Ready')

def handle_client (clientSocket):
    while True:
        try:
            clientData = clientSocket.recv(4096)
        except  OSError:
            print("Client disconnected")
            clientSocket.close()
            break
        if not clientData:
            print("Client disconnected")
            clientSocket.close()
            break
        else:
            print("Sending client data to server....")
            try:
                serverSocket.sendall(clientData)
            except BrokenPipeError:
                print("Server disconnected")
                serverSocket.close()
                clientSocket.close()
                os._exit(0)
            serverData = serverSocket.recv(2048)
            if not serverData:
                print("Server disconnected")
                serverSocket.close()
                clientSocket.close()
                os._exit(0)
            print("Sending server data to client ...")
            clientSocket.sendall(serverData)


while True:
    connectionSocket, address = clientSocket.accept()
    Thread(target=handle_client,args=(connectionSocket,)).start()


