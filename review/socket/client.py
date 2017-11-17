import socket
sk = socket.socket()
address = ('127.0.0.1',8991)
sk.connect(address)



while 1:
	inp = input('<<<')
	sk.sendall(bytes(inp,'utf8'))
	res_len = int(sk.recv(1024).decode()) #长度
	sk.sendall(bytes('ok','utf8'))
	data = bytes()
	while len(data) != res_len:
		recv = sk.recv(1024)
		data += recv
	print(str(recv, 'utf8'))

sk.close()