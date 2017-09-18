'''
A web server that handles one HTTP request at a time.

This web server should accept and parse the HTTP request, get the requested file from the server's file system,
create an HTTP response message consisting of the requested file preceded by header lines,
and then send the response directly to the client.

If the requested file is not present to the server, the server should send an HTTP "404 Not Found" message
back to the client
'''


from socket import * #import socket module
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) # Create a server socket
#Prepare a server socket
serverPort = 13000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, address = serverSocket.accept() # Called when client knocks
    print('address:', address)
    try:
        # Open and read the requested html file
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read()

        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        print('200 OK')

        # Send the content of the requested file to the client
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close() # Close connection socket

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><title>404 not found</title><body><h1>404 Not Found</h1></body></html>\r\n")
        print('404 Not Found')

        connectionSocket.close() # Close connection socket

    serverSocket.close() # Close server initial socket
    sys.exit() # Terminate the program after sending the corresponding data
