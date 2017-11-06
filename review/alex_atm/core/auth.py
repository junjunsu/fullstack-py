from core import db_handler
import time

def login_required(func):
	#验证用户登录
	def warpper(*args,**kwargs):
		if args[0].get('is_authenticated'):
			return func(*args,**kwargs)
		else:
			exit("User is not authenticated.")
	return warpper

def acc_auth2(account , password):
	'''
	优化版认证接口
	:param account:
	:param password:
	:return:
	'''
	db_api = db_handler.db_handler()
	data = db_api("select * from accounts where account=%s"% account)

	if data['password'] == password:
		exp_time_stamp = time.mktime(time.strptime(data['expire_date'],"%Y-%m-%d"))
		if time.time() > exp_time_stamp:
			print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
		else:
			return data
	else:
		print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(user_data,log_obj):
	'''
	account login func
	:param user_data:  user info data , only saves in memory
	:param log_obj:
	:return:
	'''
	retry_count = 0
	while user_data['is_authenticated'] is not True and retry_count < 3:
		account = input("\033[32;1maccount:\033[0m").strip()
		password = input("\033[32;1mpassword:\033[0m").strip()
		auth = acc_auth2(account , password) #输入用户名密码吧数据给他
		if auth:
			user_data['is_authenticated'] = True
			user_data['account_id'] = account
			#print("welcome")
			return auth
		retry_count +=1
	else:
		log_obj.error("account [%s] too many login attempts" % account)
		exit()

















