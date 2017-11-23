#传送命令对方执行
#我这边发一个命令,你那边执行了,把结果给我看


import socket,subprocess,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sk = socket.socket()
address = ('127.0.0.1',8002)
sk.bind(address)
sk.listen(3)

print('waiting........')
while 1:
	conn, addr = sk.accept()
	while 1:
		data = conn.recv(1024)
		#解析数据
		cmd,filename,filesize = str(data,'utf8').split('|')
		path = os.path.join(BASE_DIR,'upload',filename)
		filesize = int(filesize)

		f = open(path,'ab')
		#循环接收
		has_receive = 0
		while has_receive != filesize:
			data = conn.recv(1024)
			f.write(data)
			has_receive += len(data)   #试一下bytes长度跟字符串长度一样吗?一样的

sk.close()































