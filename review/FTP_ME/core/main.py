#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: main.py 
@time: 2017/12/02 
"""
from core import auth
from core import logger
from config import settings
import socketserver
import subprocess
access_logger = logger.logger('access')





user_data = {
	'user_id':None,
	'is_authenticated':False,
	'user_data':None,
}



class FtpServer( socketserver.BaseRequestHandler ):
	def handle( self ):
		print( "服务端启动!" )
		logout = False
		while True:
			conn = self.request
			print( self.client_address )
			while not logout:
				user_name = conn.recv( 1024 ).decode( 'utf8' )
				print(user_name)
				data = auth.acc_login( user_data )
				if data:
					res = user_name.split(' ')
					print(res)
					obj = subprocess.Popen(res,stdout = subprocess.PIPE)
					cmd_result = obj.stdout.read()
					print(cmd_result)
					#首先把长度给他
					cmd_size = str(len(cmd_result))
					conn.sendall(cmd_size.encode('utf8'))
					conn.recv(1024)
					conn.sendall( cmd_result )

			conn.close()


class HandleFtp():
	def __init__( self ):
		self.address = settings.FTP_INFO['ip_address']
		self.port = settings.FTP_INFO['port']

	def connect_server( self ):
		server = socketserver.ThreadingTCPServer( (self.address, self.port), FtpServer )
		server.serve_forever()


def run():
	obj = HandleFtp()
	res = obj.connect_server()
	# data = auth.acc_login(user_data)
	# if user_data['is_authenticated']:
	# 	user_data['user_data'] = data
	# 	interactive( user_data )

