"""
    Sa marche 
    - Si plusiere clients essaie de contacter le serveur il seront bloquer , traitement de séquentiel. 
    - Essaie de le faire avec les thread
"""
from socket import *
from time import *
from threading import *
from os.path import exists


clientPort_listening = 2020

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort_listening))
clientSocket.listen(4)

serverName = '127.0.0.1'
serverPort = 8000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.connect((serverName,serverPort))

print ('Relayer Ready')
sleep(60)

def handle_client (clientSocket):
    while True:
        try:
            request = clientSocket.recv(1024).decode()
        except  OSError:
            clientSocket.close()
            break
        if not request:
            clientSocket.close()
            break
        else:
           # Parse HTTP headers
            headers = request.split('\n')
            filename = headers[0].split()[1]
            file_exists = exists("cache/"+filename[1:])
            if(file_exists):
                 fin = open("cache/"+filename[1:]) 
                 content = fin.read()
                 fin.close()
                 response = 'HTTP/1.0 200 OK\n\n' + content
                 clientSocket.send(response)  
            else:
                
                serverSocket.sendall(request.encode("utf-8"))
                serverData = serverSocket.recv(2048)
                file = open(filename[1:],"w")
                file.write(serverData)
                file.close()
                clientSocket.send(serverData)


while True:
    connectionSocket, address = clientSocket.accept()
    Thread(target=handle_client,args=(connectionSocket,)).start()
    #handle_client(connectionSocket)


