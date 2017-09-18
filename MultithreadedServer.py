'''
https://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
'''


from socket import * #import socket module
import sys # In order to terminate the program
import threading


class ClientThread(threading.Thread):
    def __init__(self, connectSkt):
        threading.Thread.__init__(self)
        self.connectionSocket = connectSkt
    def run(self):
        while True:
            try:
                # Open and read the requested html file
                message = self.connectionSocket.recv(1024)

                if not message:
                    print('received non-msg')
                    break

                filename = message.split()[1]
                f = open(filename[1:])
                outputData = f.read()

                # Send one HTTP header line into socket
                self.connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

                # Send the content of the requested file to the client
                for i in range(0, len(outputData)):
                    self.connectionSocket.send(outputData[i].encode())
                self.connectionSocket.send("\r\n".encode())

                #self.connectionSocket.close()  # Close connection socket

            except IOError:
                # Send response message for file not found
                self.connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
                self.connectionSocket.send("<html><head></head><title>404 not found</title><body><h1>404 Not Found</h1></body></html>\r\n")
                print('404 Not Found')
                #self.connectionSocket.close()  # Close connection socket



if __name__ == '__main__':
    thread_list = [] # List to keep track of threads
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Create the initial server socket
    # Prepare the server socket
    serverPort = 25000
    serverSocket.bind(('', serverPort))
    serverSocket.listen(10) #max connections

    while True:
        print('Ready to serve...')
        connectionSocket, address = serverSocket.accept() # Called when client knocks
        print('address:', address)

        client_thread = ClientThread(connectionSocket)
        client_thread.start() # Runs the thread
        thread_list.append(client_thread)



