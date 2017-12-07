#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: db_handler.py 
@time: 2017/12/02 
"""
from config import settings
import os,json
class DbHandler(object):
	conn_params = settings.DATEBASE

	def __init__(self):
		pass
	@classmethod
	def db_handler(cls):
		if cls.conn_params['engine'] == 'file_storage':
			return cls.file_db_handle()
		elif cls.conn_params['engine'] == 'mysql':
			pass
	@classmethod
	def file_db_handle(cls):
		return cls.file_execute
	@classmethod
	def file_execute(cls,sql,**kwargs):
		db_path = os.path.join(cls.conn_params['path'],cls.conn_params['name'])
		sql_list = sql.split("where")
		if sql_list[0].startswith("select") and len(sql_list) > 1:
			return cls.read_data(db_path,sql_list)
		elif sql_list[0].startswith("update") and len(sql_list) > 1:
			return cls.write_data(db_path,sql_list)


	@classmethod
	def read_data(cls,db_path,sql_list):
		column, val = sql_list[1].strip().split( "=" )
		if column == 'user_data':

			user_data_file = '.'.join( [os.path.join( db_path, val ), 'json'] )
			if os.path.exists( user_data_file ) and os.path.isfile( user_data_file ):
				with open( user_data_file, 'r' ) as f:
					user_data = json.load( f )
					return user_data
			else:
				exit( "\033[32;1mData [%s] does not exist!\033[0m" % val )
	@classmethod
	def write_data(cls,db_path,sql_list):
		pass









