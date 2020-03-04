import socket

HOST = '169.254.1.1'
PORT = 3101
dest = (HOST,PORT)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("não foi possível criar o socket")
	exit()

msg = '+++'.encode()

while True:
	try:
		s.sendto(msg, (dest))
		data, ip = s.recvfrom(1024)
		print("{}: {}".format(ip, data.decode()))

	except socket.error:
		print("Falha ao enviar/receber mensagem")
		exit()
