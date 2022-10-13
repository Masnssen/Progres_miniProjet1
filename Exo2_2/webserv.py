from genericpath import exists
from socket import *
from pathlib import Path


def findFille(file_name):
    print(file_name)
    txt = ""
    if exists(file_name):
        if Path(file_name).is_file():
            f = open(file_name, 'r')
            txt = f.read()
            f.close()

    return txt

def analyseRequete(request):
    listeParam = request.split(" ")
    if len(listeParam) >= 3 and listeParam[0].upper() == "GET":
        return listeParam[1]
    return ""
    

SERVER_PORT = 8080

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('', SERVER_PORT))

#time.sleep(60)
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)


connectionSocket, address = server_socket.accept()

while True:

    request = connectionSocket.recv(2048).decode("utf-8")
    # Parse HTTP headers
    if not request:
        print("relayer déconnecter")
        connectionSocket.close()
        break

    filename = analyseRequete(request)
    
    # Get the content of the file
    if filename == '/' or filename == "":
        filename = '/index.html'
    
    content = findFille(filename[1:])
    if content == "":
        content = "<!DOCTYPE html><html>File Not Found</html>"
        response = 'HTTP/1.1 404 NOT FOUND\nContent-Type:text/html\nContent-Length:'+str(len(content)) +'\n\n' + content
    else:
        response = 'HTTP/1.1 200 OK\nContent-Type:text/html\nContent-Length:'+str(len(content)) +'\n\n'+ content
    
    # Send HTTP response
    connectionSocket.sendall(response.encode("utf-8"))
    
# Close socket
server_socket.close()
        
    