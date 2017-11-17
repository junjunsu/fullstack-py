import socket
sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)

print('waiting........')



#第一种
# while not talk_flag:
# 	#接收信息
# 	data = conn.recv(1024)
# 	print('.........',str(data,'utf8'))
# 	if not data:
# 		conn.close()
# 		conn, addr = sk.accept()
# 		continue #name如果我客户端就是发个空呢,为什么让我退出
# 	#在次发送
# 	inp = input('>>>')
#
# 	conn.send(bytes(inp,'utf8'))
#
# sk.close()

#第二种
while 1:
	conn, addr = sk.accept()
	while 1:
		try:
			data = conn.recv(1024)
		except Exception:
			break
		if not data:break
		print('.........',str(data,'utf8'))
		inp = input('>>>')
		conn.send(bytes(inp,'utf8'))
sk.close()






























