from conf import settings
import os ,json
def file_execute(sql,**kwargs):
	conn_params = settings.DATABASE
	#select * from accounts where account=%s
	db_path = '%s/%s'%(conn_params['path'], conn_params['name'])

	#print(sql,db_path)
	sql_list = sql.split("where")
	#print(sql_list)
	if sql_list[0].startswith("select") and len(sql_list) > 1:
		column,val = sql_list[1].strip().split("=")
		if column == 'account':
			account_file = "%s/%s.json"%(db_path, val)
			#print(account_file)
			if os.path.isfile(account_file):
				with open(account_file,'r') as f:
					account_data = json.load(f)
					return account_data
			else:
				exit("\033[32;1mAccount [%s] does not exist!\033[0m" % val )
	elif sql_list[0].startswith("update") and len(sql_list) > 1:
		column,val = sql_list[1].strip().split("=")
		#print(column) #account
		#print(val)   #1234

		if column == 'account':
			account_file = "%s/%s.json"%(db_path, val)
			if os.path.isfile(account_file):
				account_data = kwargs.get('account_data')

				# print(account_data)
				# exit()
				with open(account_file,'w') as f:
					acc_data = json.dump(account_data,f)
					return True









def file_db_handle(conn_params):
	#print('file db:',conn_params)
	return file_execute


def db_handler():
	"""
	connect to db
	:return:
	"""
	conn_params = settings.DATABASE
	if conn_params['engine'] == 'file_storage':
		return file_db_handle(conn_params)
	elif conn_params['engine'] == 'mysql':
		pass #todo

def handle_log(account_id):
	conn_params = settings.LOG_PATH
	file_name = settings.LOG_TYPES['transaction']
	# select * from accounts where account=%s
	file_path = '%s/%s' % (conn_params['path'],file_name)
	if os.path.isfile(file_path):
		with open(file_path, 'r') as f:
			account_data = f.read()
			return account_data
	else:
		exit("\033[32;1mAccount [%s] does not exist!\033[0m" % val)
