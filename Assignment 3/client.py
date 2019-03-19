#client.py
from socket import *
sName = 'localhost'
sPort = 11000
cSocket = socket(AF_INET,SOCK_STREAM)
cSocket.connect((sName,sPort))

sentence = input("Input a number:")
cSocket.send(sentence.encode())

modifiedSentence = cSocket.recv(1024)
print("From Server:",modifiedSentence.decode())

cSocket.close()