import socket
import sys
import time

CL_HOST = '169.254.1.1'
CL_PORT = 2101
cl_addr = ((CL_HOST, CL_PORT))

SV_HOST = ''
SV_PORT = 5000
sv_addr = ((SV_HOST, SV_PORT))

try:
	cl_socket = socket.socket(socket.AF_INET,
			   	  socket.SOCK_STREAM)
	cl_socket.connect(cl_addr)
except socket.error:
	print("Falha na criação do socket cliente")
	sys.exit()

print("Socket cliente estabelecido")

try:
	sv_socket = socket.socket(socket.AF_INET,
				  socket.SOCK_STREAM)
	sv_socket.bind(sv_addr)
	sv_socket.listen(1)
except socket.error:
	print("Falha na criação do socket servidor")
	sys.exit()

print("Socket servidor estabelecido")

conn, client = sv_socket.accept()
print("Cliente conectado: {}".format(client))

#msg = 'Hello World!'.encode()

while True:
	packet = (cl_socket.recv(4096))
	print(packet)

	try:
		conn.send(packet)
	except socket.error:
		print("Erro no envio")
		conn.close()
