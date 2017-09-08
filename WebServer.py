'''
A web server that handles one HTTP request at a time.

This web server should accept and parse the HTTP request, get the requested file from the server's file system,
create an HTTP response message consisiting of the requested file preceded by headerlines,
and then send the response directly to the client.

If the requested file is not present to the server, the server should send an HTTP "404 Not Found" message
back to the client
'''


from socket import * #import socket module
import sys # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket

#FILL IN START ------------------------------
serverName = 'serverName'
serverPort = 12000
serverSocket.bind(('', 12000))
serverSocket.listen(1)
#FILL IN END ------------------------------

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()#Fill in start    #Fill in end

        #Send one HTTP header line into socket

        # FILL IN START ------------------------------
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
        # FILL IN END --------------------------------

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:

        # Send response message for file not found
        # FILL IN START ------------------------------
        connectionSocket.send('404 Not Found')
        # FILL IN END --------------------------------
        #Close client socket

        # FILL IN START ------------------------------
        connectionSocket.close()
        # FILL IN END --------------------------------
    serverSocket.close()
    sys.exit() #Terminate the program after sending the corresponding data
