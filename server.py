import socket
import sys

cl_host = '169.254.1.1'
cl_port = 2101
cl_addr = (cl_host, cl_port)

sv_host = ''
sv_port = 5000
sv_addr = (sv_host, sv_port)

try:
	cl_socket = socket.socket(socket.AF_INET,
				  socket.SOCK_STREAM)
	cl_socket.connect(cl_addr)
except socket.error:
	print('Falha no acesso ao socket cliente')
	sys.exit()
print('Socket cliente acessado')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sv_s:
	sv_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sv_s.bind(('', 5000))
	sv_s.listen(5)
	conn, addr = sv_s.accept()
	conn.send('WELCOME\n(isto veio do servidor)\n'.encode())
	while True:
		packet = str(cl_socket.recv(1024))
		print(packet)
		data = conn.recv(1024).decode()
		conn.send('(isto veio do servidor)... Menssagem {} {}\n'.format(data, index).encode('utf-8'))
		conn.send('Pacote: {}'.format(packet))
