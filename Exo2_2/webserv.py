from socket import *
#import time

SERVER_PORT = 8000

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
server_socket.bind(('', SERVER_PORT))
#time.sleep(60)
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)


connectionSocket, address = server_socket.accept()

while True:

    request = connectionSocket.recv(2048).decode()
   
    
    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]
    
    # Get the content of the file
    if filename == '/':
        filename = '/index.html'
    try:
        fin = open(filename[1:])
        content = fin.read()

        fin.close()
        print(content)
        response = "HTTP/1.1 200 OK\nContent-Type : text/html\n\n" + content
    except FileNotFoundError:
        response = 'HTTP/1.1 404 NOT FOUND\nContent-Type:text/html\n\nFile Not Found'
    
    # Send HTTP response
    connectionSocket.sendall(response.encode("utf-8"))
    
# Close socket
server_socket.close()
        
    