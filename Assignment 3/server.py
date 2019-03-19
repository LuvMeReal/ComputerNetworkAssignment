#server.py
from socket import *
sPort = 11000
sSocket = socket(AF_INET,SOCK_STREAM)
sSocket.bind(('localhost',sPort))
sSocket.listen(1)

print ("Ready to receive...")

while True:
	connectionSocket, addr = sSocket.accept()

	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = str(int(sentence,10)*10)
	connectionSocket.send(capitalizedSentence.encode())

	connectionSocket.close()