# Cliente para o departamento de geografia
# Departamento do aluno Rodrigo Fontes Martins - 201600092495

from socket import *

servidor = ('0.0.0.0', 22203)

cliente = socket (AF_INET, SOCK_STREAM) 
cliente.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cliente.connect(servidor)

request = 'GET / HTTP/1.1\r\nHost: 0.0.0.0:22203\r\nclima: tropical\r\n'.encode()
# request = 'GET / HTTP/1.1\r\nHost: 0.0.0.0:22203\r\nclima: semiarido\r\n'.encode()

response = ''

cliente.sendall(request)

try:	
	recv = cliente.recv(1024)
	response += recv.decode()
	print(response)
except Exception as E:
	print(E)
		
cliente.close()