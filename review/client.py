#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: client.py 
@time: 2017/12/02 
"""
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8098))

lock = False
while not lock:
	inp = input('>>>>用户名:').strip()
	sk.sendall(inp.encode('utf8'))
	cmd_size = int(sk.recv(1024).decode('utf8'))
	sk.sendall('ok'.encode('utf8'))
	data = bytes()
	while len(data) != cmd_size:
		recv = sk.recv(1024)
		data += recv
	print(recv.decode('utf8'))










