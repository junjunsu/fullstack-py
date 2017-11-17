import socket,os,sys
sk = socket.socket()
#print(sk)
address = ('127.0.0.1',8000)
sk.connect(address)


talk_flag = False

while not talk_flag:
	inp = input('>>>')
	if inp == '.':
		talk_flag = True
	else:
		sk.send(bytes(inp,'utf8')) #空发送过去了,对方一看是空,会阻塞,知道你下次发一个值过来
		#sk.send(bytes('yyy','utf8'))
		data = sk.recv(1024)
		print(str(data,'utf8'))


sk.close()






#不可以发空,发空相当于阻塞状态,是发送过去了,单recv看到你是个空,他不做任何处理,等待你下次发一个值过来在处理


