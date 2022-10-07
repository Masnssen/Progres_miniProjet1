"""
    Sa marche 
    - Si plusiere clients essaie de contacter le serveur il seront bloquer , traitement de séquentiel. 
    - Essaie de le faire avec les thread
"""
from socket import *
from time import *
from threading import *
from os.path import exists
import os, os.path


clientPort_listening = 2020

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort_listening))
clientSocket.listen(4)

serverName = '127.0.0.1'
serverPort = 8000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.connect((serverName,serverPort))

print ('Relayer Ready')


def handle_client (clientSocket):
    while True:
        try:
            request = clientSocket.recv(2028).decode("utf-8")
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
            file_exists = exists("cacheDir/"+filename[1:])
            print(file_exists)
            if(file_exists):
                 fin = open("cacheDir/"+filename[1:]) 
                 content = fin.read()
                 fin.close()
                 response = content
                 clientSocket.sendall(response.encode("utf-8"),)  
                 clientSocket.close()
                 break
            else:
                serverSocket.sendall(request.encode("utf-8"))
                serverData = serverSocket.recv(2048)
                def safe_open_w(path):
                    #open "path" en w, create dir if needed
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    return open(path, 'w')

                with safe_open_w('cacheDir/'+filename[1:]) as f:
                    f.write(serverData.decode("utf-8"))

                #file = open("cacheDir/"+filename[1:],"w")
                #file.write(serverData.decode("utf-8"))
                f.close()
                print(serverData.decode("utf-8"))
                clientSocket.sendall(serverData)
                clientSocket.close()
                break


while True:
    connectionSocket, address = clientSocket.accept()
    Thread(target=handle_client,args=(connectionSocket,)).start()
    #handle_client(connectionSocket)


