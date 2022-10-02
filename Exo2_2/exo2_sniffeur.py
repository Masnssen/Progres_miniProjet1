from socket import *
from time import *
from threading import *
import json

clientPort_listening = 8888

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort_listening))
clientSocket.listen(4)

serverName = '127.0.0.1'
serverPort = 8000

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
            print(address[0])
            if(file_name[1:] != ""):
                #Ajouter la requete et le client dans le fichier
                file = open("log","r")
                data = file.read()
                file.close()
                print("Les donnees", data)
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
                    data = {file_name: {address[0] : [False, 0]}}
                    print(data)
                    data = json.dumps(data)
                    
                file = open("log", "w")
                file.write(data)
                file.close()

                serverSocket.sendall(request.encode("utf-8"))
                serverData = serverSocket.recv(2048)

                if serverData.decode("utf-8").split(" ")[1] != "404":
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

                print(serverData.decode("utf-8"))
                clientSocket.sendall(serverData)
                clientSocket.close()
                break
            else:
                clientSocket.close()
                break



while True:
    connectionSocket, address = clientSocket.accept()
    Thread(target=handle_client,args=(connectionSocket, address,)).start()
    #handle_client(connectionSocket)
