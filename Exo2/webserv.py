from socket import *
#import time

SERVER_PORT = 8000

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
server_socket.bind(('', SERVER_PORT))
#time.sleep(60)
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)



while True:
    connectionSocket, address = server_socket.accept()
    request = connectionSocket.recv(1024).decode()
    print(request)
    
    
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

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:

        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
    
    
    # Send HTTP response
    connectionSocket.sendall(response.encode())
    
# Close socket
server_socket.close()
        
    