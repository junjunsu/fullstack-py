#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: auth.py 
@time: 2017/12/02
输入用户名 密码
登录到自己的home目录
"""
from core.db_handler import DbHandler
import time
def verify_login(user_name,passwd):
	file_handle = DbHandler.db_handler()
	data = file_handle("select * from accounts where user_data=%s"% user_name)
	if data['password'] == passwd:
		exp_time_stamp = time.mktime(time.strptime(data['expire_date'],'%Y-%m-%d'))
		if time.time() > exp_time_stamp:
			print( "\033[32;1mAccount [%s] has expired!\033[0m" % user_name )
		else:
			return data
	else:
		print( "\033[32;1musername or password is incorrect!\033[0m" )



def acc_login(user_data):
	retry_count = 0
	auth = verify_login(1234,'abc')
	if auth:
		user_data['is_authenticated'] = True
		user_data['username'] = 1234
	return auth
	# while user_data['is_authenticated'] is not True and retry_count < 3:
	# 	user_name = input("\033[32;1m用户名:\033[0m").strip()
	# 	passwd = input("\033[32;1m密码:\033[0m").strip()
	# 	auth = verify_login(user_name,passwd)
	# 	if auth:
	# 		user_data['is_authenticated'] = True
	# 		user_data['username'] = user_name
	# 		return auth
	# 	else:
	# 		print('输入错误')
	# 	retry_count +=1
	# else:
	# 	exit("username [%s] too many login attempts" % user_name)

if __name__ == '__main__':
    pass