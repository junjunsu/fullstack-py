#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: ftp_server.py 
@time: 2017/12/02 
"""
import socketserver
import subprocess
from config import settings
class FtpServer(socketserver.BaseRequestHandler):
	def handle(self):
		print("服务端启动!")
		logout = False
		while True:
			conn = self.request
			print(self.client_address)
			while not logout:
				user_name =  conn.recv(1024).decode('utf8')


			conn.close()


class HandleFtp():
	def __init__(self):
		self.address = settings.FTP_INFO['ip_address']
		self.port = settings.FTP_INFO['port']
	def connect_server(self):
		server = socketserver.ThreadingTCPServer((self.address,self.port),FtpServer)
		server.serve_forever()


if __name__ == '__main__':

    pass