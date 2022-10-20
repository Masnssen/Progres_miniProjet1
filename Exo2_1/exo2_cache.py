from socket import *
from time import *
from threading import *
from pathlib import Path
import os, os.path


clientPort_listening = 4444

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort_listening))
clientSocket.listen(1)

serverName = '127.0.0.1'
serverPort = 4040

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.connect((serverName,serverPort))

print ('Cache Ready')

def safe_open_w(path):
    #open "path" en w, create dir if needed
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')


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
            
            if filename[1:] == "":
                file_exists = False
            else:
                file_exists = Path("cacheDir/"+filename[1:]).is_file()
            if(file_exists):
                fin = open("cacheDir/"+filename[1:]) 
                content = fin.read()
                fin.close()
                response = content
                clientSocket.sendall(response.encode("utf-8"),)  
            else:
                serverSocket.sendall(request.encode("utf-8"))
                serverData = serverSocket.recv(2048)
                if not serverData:
                    serverSocket.close()
                    clientSocket.sendall("Error serveur non disponible ".encode("utf-8")) 
                    clientSocket.close()
                    print("Le serveur n'est pas disponible")
                    os._exit(0)
                    break
                if serverData.decode("utf-8").split(" ")[1] == "200":
                    with safe_open_w('cacheDir/'+filename[1:]) as f:
                        f.write(serverData.decode("utf-8"))
                        f.close()
                        
                clientSocket.sendall(serverData)
               
                
while True:
    connectionSocket, address = clientSocket.accept()
    Thread(target=handle_client,args=(connectionSocket,)).start()
    


