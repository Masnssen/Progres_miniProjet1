"""
    Ajouter si fichier log n'existe pas le cree vide 
"""

from socket import *
from time import *
from threading import *
import json
from pathlib import Path
import os

clientPort_listening = 9666

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort_listening))
clientSocket.listen(4)

serverName = '127.0.0.1'
serverPort = 9888

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.connect((serverName,serverPort))

print ('Relayer Ready')

def analyseRequete(request):
    listeParam = request.split(" ")
    if len(listeParam) >= 3 and listeParam[0].upper() == "GET":
        return listeParam[1]
    return ""
    

def handle_client (clientSocket, address):
    
    while True:
        try:
            request = clientSocket.recv(2048).decode("utf-8")
        except  OSError:
            clientSocket.close()
            break
        if not request:
            clientSocket.close()
            break
        else:
            # Parse HTTP headers
            file_name = analyseRequete(request)
            
            if(file_name != ""):
                #Ajouter le fichier log s'il n'existe pas 
                if not Path("log").is_file():
                    file = open("log", "w")
                    file.close()

                #Ajouter la requete et le client dans le fichier
                file = open("log","r")
                data = file.read()
                file.close()
                
                if data != "":
                    data = json.loads(data)
                    if file_name in data:
                        if address[0] in data[file_name]:
                            data[file_name][address[0]][1] += 1
                            data = json.dumps(data)
                        else:
                            data[file_name].update({address[0] : [False, 1]})
                            data = json.dumps(data)
                    else:
                        data.update({file_name : {address[0] : [False, 1]}})
                        data = json.dumps(data)
                else:
                    data = {file_name: {address[0] : [False, 1]}}
                    data = json.dumps(data)
                    
                file = open("log", "w")
                file.write(data)
                file.close()

                serverSocket.sendall(request.encode("utf-8"))
                serverData = serverSocket.recv(2048)
        
                if not serverData:
                    serverSocket.close()
                    clientSocket.sendall("Error serveur non disponible ".encode("utf-8")) 
                    clientSocket.close()
                    print("Le serveur n'est pas disponible")
                    os._exit(0)
                    break

                if len(serverData.decode("utf-8").split(" ")) > 2 and serverData.decode("utf-8").split(" ")[1] != "404":
                    file = open("log", "r")
                    data = file.read()
                    file.close()
                    data = json.loads(data)
                    if file_name in data and address[0] in data[file_name] and data[file_name][address[0]][0] == False:
                        data[file_name][address[0]][0] = True
                        data = json.dumps(data)
                        file = open("log", "w")
                        file.write(data)
                        file.close()

                clientSocket.sendall(serverData) 
            else:
                clientSocket.sendall("Error not http request".encode("utf-8")) 
                clientSocket.close()
                break




while True:
    connectionSocket, address = clientSocket.accept()
    Thread(target=handle_client,args=(connectionSocket, address,)).start()
    #handle_client(connectionSocket)
