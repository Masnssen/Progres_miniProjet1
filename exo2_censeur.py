from socket import *
from time import *
from threading import *
import json

clientPort_listening = 8080

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
    if len(listeParam) >= 3 and listeParam[0].upper() == "GET" and listeParam[2][0:4].upper() == "HTTP":
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
                #check if not in blacklist
                file = open("config","r")
                data = file.read()
                file.close()
                #print("les liens blacklisté : ", data["blacklist"])
                data = json.loads(data)
                if file_name in data:
                    #fin = open('forbiden.txt','r')
                    #content = fin.read()
                    #fin.close()
                    content = "acces interdit!!!!!!!!!!"
                    response = "HTTP/1.1 403 OK\nContent-Type : text/html\n\n" + content 
                    clientSocket.sendall(response.encode("utf-8"))
                    clientSocket.close()
                else:
                    serverSocket.sendall(request.encode("utf-8"))
                    serverData = serverSocket.recv(2048)
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