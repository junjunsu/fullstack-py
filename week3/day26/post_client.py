import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1',8001)
sk.connect(address)


talk_flag = False

while True:
	inp = input('>>>')
	if inp == '.':
		break

	sk.send(bytes(inp,'utf8')) #int(
	result_len = int(str(sk.recv(1024),'utf8')) #
	sk.sendall(bytes('ok','utf8'))
	#print(result_len,type(result_len))  #str 169
	data = bytes()  #跟sum = 0 是一样的
	while  len(data) != result_len:
		recv = sk.recv(1024)
		data += recv
	print(str(recv, 'utf8'))
sk.close()






















