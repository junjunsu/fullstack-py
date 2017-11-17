import socket,subprocess
sk = socket.socket()
address = ('127.0.0.1',8991)
sk.bind(address)
sk.listen(3)
print('waiting.....')
conn,address = sk.accept()


while True:
	data = conn.recv(1024)
	if not data:break
	cmd = data.decode()
	obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	res = obj.stdout.read()
	#先计算一下长度
	result_len = bytes(str(len(res)),'utf8')
	print('>>>>>>',result_len)
	conn.sendall(result_len)
	conn.recv(1024)
	conn.sendall(res)
sk.close()



