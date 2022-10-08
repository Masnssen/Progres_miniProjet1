from socket import *
from time import *
from threading import *

clientPort_listening = 3000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort_listening))
clientSocket.listen(1)

serverName = '127.0.0.1'
serverPort = 7000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.connect((serverName,serverPort))

print ('Relayer Ready')

def handle_client (clientSocket):
    while True:
        try:
            clientData = clientSocket.recv(4096)
        except  OSError:
            clientSocket.close()
            break
        if not clientData:
            clientSocket.close()
            break
        else:
            serverSocket.sendall(clientData)
            serverData = serverSocket.recv(2048)
            clientSocket.sendall(serverData)


while True:
    connectionSocket, address = clientSocket.accept()
    Thread(target=handle_client,args=(connectionSocket,)).start()


