import socket
import sys

HOST = '169.254.1.1'
#HOST = '10.72.10.84'
PORT = 2101

try:
	tcp = socket.socket(socket.AF_INET,
			    socket.SOCK_STREAM)

except socket.error:
	print("Falha na criação do socket")
	sys.exit()

print("Socket estabelecido")

dest = ((HOST, PORT))

try:
	tcp.connect(dest)
except socket.error:
	print("Falha na conexão")
	sys.exit()

print("Conectado ao servidor")

"""
msg = '+++'.encode()

try:
	tcp.sendall(msg)
except socket.error:
	print("Falha na transmissão")
	sys.exit()

print("Mensagem enviada")
"""

while True:
	resp = tcp.recv(4096)
	print(resp)

tcp.close()
