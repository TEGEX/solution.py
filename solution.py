#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):


    while True:
        #Establish the connection
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(("", port))
        serverSocket.listen(1)
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
        try:
            message = connectionSocket.recv(1024) #Fill in start    #Fill in end
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()#Fill in start     #Fill in end
            print (outputdata)
            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
            connectionSocket.send(outputdata)
            #Fill in end

            #Send the content of the requested file to the client
            connectionSocket.close()

        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
            #Fill in end

            #Close client socket
            #Fill in start

            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
