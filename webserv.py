from genericpath import exists, isfile
from socket import *
from pathlib import Path

SERVER_PORT = 9999

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
server_socket.bind(('', SERVER_PORT))
#time.sleep(60)
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)


connectionSocket, address = server_socket.accept()

#Find fille and return her contente , else return ""
def findFille(file_name):
    
    txt = ""
    if exists(file_name):
        if Path(file_name).is_file():
            f = open(file_name, 'r')
            txt = f.read().decode("utf-8")
            f.close()
    
    return txt
        
while True:

    request = connectionSocket.recv(2048).decode()
    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
        filename = '/index.html'
   
    #Verifier qu'il existe et si bien un fichier 
    content = findFille(filename[1:])
    if content != "":
        response = "HTTP/1.1 200 OK\nContent-Type : text/html\n\n" + content
    else:
        response = 'HTTP/1.1 404 NOT FOUND\nContent-Type:text/html\n\nFile Not Found\n\n'

    # Send HTTP response
    print("La reponse", response)
    connectionSocket.sendall(response.encode("utf-8"))
    
    
# Close socket
server_socket.close()
        
    