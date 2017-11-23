from core import auth
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required

trans_logger = logger.logger('transaction')

access_logger = logger.logger('access')
user_data = {
	'account_id':None,
	'is_authenticated':False,
	'account_data':None,
}
@login_required
def account_info(acc_data):
	user_info = acc_data['account_data']
	current_info = '''
	 ----------USER INFO----------
		\033[32;1mUser : %s
		Balance : %s
		ExpireTime : %s
		EnrollDate : %s
	\033[0m''' %(user_info['id'],user_info['balance'],user_info['expire_date'],user_info['enroll_date'])
	back_flag = False
	while not back_flag:
		print(current_info)
		option = input("如果返回按b")
		if option == 'b':
			back_flag = True
@login_required
def repay(acc_data):
	'''
	还款
	:param acc_data:
	:return:
	'''
	account_data = accounts.load_current_balance(acc_data['account_id'])
	# print(account_data)
	# exit()
	current_balance = ''' --------- BALANCE INFO --------
	        Credit :    %s
	        Balance:    %s''' % (account_data['credit'], account_data['balance'])
	print(current_balance)

	back_flag = False
	while not back_flag:
		repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
		if len(repay_amount) >0 and repay_amount.isdigit():
			#print('ddd 00')
			new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)
			if new_balance:
				print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
		else:
			print('\033[32;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)

		if repay_amount == 'b':
			back_flag = True
#减钱
@login_required
def withdraw(acc_data):
	'''
	提现
	:return:
	'''
	#获取当前最新的账户信息
	account_info = accounts.load_current_balance(acc_data['account_id'])
	current_balance = ''' --------- BALANCE INFO --------
		        Credit :    %s
		        Balance:    %s''' % (account_info['credit'], account_info['balance'])
	print(current_balance)

	back_flag = False
	while not back_flag: #如果 back_flag 没有值(是flase)得话走循环
		withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
		if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
			new_balance = transaction.make_transaction(trans_logger,account_info,'withdraw',withdraw_amount)
			if new_balance:
				print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
		else:
			print('\033[32;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)
		if withdraw_amount == 'b':
			back_flag = True
#转账
@login_required
def transfer(acc_data):
	# 获取当前最新的账户信息
	account_info = accounts.load_current_balance(acc_data['account_id'])

	current_balance = ''' --------- BALANCE INFO --------
			        Credit :    %s
			        Balance:    %s''' % (account_info['credit'], account_info['balance'])
	print(current_balance)
	back_flag = False
	while not back_flag:
		trans_account_id =  input("\033[33;1mInput trans account_id:\033[0m").strip()
		trans_amount = input("\033[33;1mInput trans amount:\033[0m").strip()
		if len(trans_amount) > 0 and trans_amount.isdigit():
			trans_user_info = accounts.load_current_balance(trans_account_id)
			if trans_user_info:
				new_balance = transaction.make_transaction(trans_logger, account_info, 'transfer', trans_amount)
				new_trans_balance = transaction.make_transaction(trans_logger, trans_user_info, 'repay', trans_amount)
				if new_balance and new_trans_balance:
					print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
			else:
				print('\033[32;1m[%s] is not a valid account_id, only accept integer!\033[0m' % trans_account_id)
		else:
			print('\033[32;1m[%s] is not a valid amount, only accept integer!\033[0m' % trans_amount)
		option = input("返回请按b")
		if option == 'b':
			back_flag = True
#账单:
@login_required
def pay_check(acc_data):
	back_flag = False
	while not back_flag:
		trans_data = accounts.print_account(acc_data['account_id'])
		print('\033[32;1m['+trans_data+'\033[0m')
		option = input("如果返回按b")
		if option == 'b':
			back_flag = True

	pass
@login_required
def logout(acc_data):
	return True


#另一种方法是保持源码文件的utf-8不变，而是在’哈’前面加个u字，也就是:

# s1=u’哈’
# print s1
#
# 这样就可以正确打印出’哈’字了。
#
# 这里的这个u表示将后面跟的字符串以unicode格式存储。python会根据代码第一行标称的utf-8编码识别代码中的汉字’哈’，然后转换成unicode对象。如果我们用type查看一下’哈’的数据类
#
# 型type(‘哈’)，会得到<type ‘str’>，而type(u’哈’)，则会得到<type ‘unicode’>，也就是在字符前面加u就表明这是一个unicode对象，这个字会以unicode格式存在于内存中，而如果不加u
#
# ，表明这仅仅是一个使用某种编码的字符串，编码格式取决于python对源码文件编码的识别，这里就是utf-8。
#
# Python在向控制台输出unicode对象的时候会自动根据输出环境的编码进行转换，但如果输出的不是unicode对象而是普通字符串，则会直接按照字符串的编码输出字符串，从而出现上面的现
#
# 象。
def interactive(acc_data):
	'''

	:param acc_data:
	:return:
	'''
	menu = u'''
	------- Oldboy Bank ---------
    \033[32;1m1.  账户信息 (已实现)
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账(已实现)
    5.  账单(半实现)
    6.  退出 (已实现)
    \033[0m'''
	menu_dic = {
		'1': account_info,
		'2': repay,
		'3': withdraw,
		'4': transfer,
		'5': pay_check,
		'6': logout,
	}
	exit_flag = False
	while not exit_flag:
		print(menu)
		user_option = input(">>:").strip()
		if user_option in menu_dic:
			#print('accdata',acc_data)
			res	= menu_dic[user_option](acc_data)
			if res is True:
				exit_flag = True
		else:
			print("\033[32;1mOption does not exist!\033[0m")
	else:
		print("欢迎下次光临!")


def run():
	acc_data = auth.acc_login(user_data,access_logger)
	if user_data['is_authenticated']:
		user_data['account_data'] = acc_data
		interactive(user_data)























