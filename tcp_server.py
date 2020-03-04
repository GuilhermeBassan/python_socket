import socket

HOST = 'localhost'
PORT = 5000

tcp = socket.socket(socket.AF_INET,
		    socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
	con, client = tcp.accept()
	print("conectado por", client)
	while True:
		msg = con.recv(1024)
		if not msg: break
		print(client, msg)
	print("Finalizando conexão do cliente", client)
	con.close()
