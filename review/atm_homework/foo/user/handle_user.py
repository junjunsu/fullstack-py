#添加用户
import json ,os
def addUser(username ,password,userinfo_path):
	if len(username) < 5 :
		return {"msg":"用户名长度不合法","error":True}
	if len(password) < 5 or not password.isdigit():
		return {"msg":"密码长度不合法","error":True}

	#判断用户文件是否存在,不存在则创建,存在则直接返回对应信息
	user_table_path = userinfo_path+'/user_table/'+username
	if not os.path.isfile(user_table_path):
		f = open(user_table_path,'w',encoding='utf8')
		user_info = {"username":username,"password":password,"auth":False}
		json.dump(user_info,f)
		f.close()
	rf = open(user_table_path,'r',encoding='utf8')
	user = json.load(rf)
	rf.close()
	return {"msg":"登陆成功", "error": False,"user_info":user}
#获取用户额度
def getUserAmount(username,path):
	user_table_path = path + '/user_table/' + username
	with open(user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		return user['card_limit']
#冻结用户
def freezeUser(username,path):
	user_table_path = path + '/user_table/' + username
	with open(user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		user['is_freze'] = True
	with open(user_table_path, 'w', encoding='utf8') as wf:
		json.dump(user, wf)


#获取该用户是否被冻结
def getUserIsfreeze(username,path):
	user_table_path = path + '/user_table/' + username
	with open(user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		return user['is_freze']

#转账接口
def transferAccount(source_username,des_username,money,path):
	#本人的
	source_user_table_path = path + '/user_table/' + source_username
	with open(source_user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		user['card_limit'] = user['card_limit'] - money
	with open(source_user_table_path, 'w', encoding='utf8') as wf:
		json.dump(user, wf)

	#目标的:
	des_user_table_path = path + '/user_table/' + source_username
	with open(des_user_table_path, 'r', encoding='utf8') as de_rf:
		user = json.load(de_rf)
		user['card_limit'] = user['card_limit'] + money
	with open(des_user_table_path, 'w', encoding='utf8') as de_wf:
		json.dump(user, de_wf)



# 扣款接口
def subAccount(username, sub_money, path):
	user_table_path = path + '/user_table/' + username
	with open(user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		user['card_limit'] = sub_money
	with open(user_table_path, 'w', encoding='utf8') as wf:
		json.dump(user, wf)


# 提现接口
def withdrawAccount(username, withdraw_money, path):
	user_table_path = path + '/user_table/' + username
	with open(user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		user['withdraw_money'] = withdraw_money * 0.05
	with open(user_table_path, 'w', encoding='utf8') as wf:
		json.dump(user, wf)


#还款接口
def addAccount(username,add_money,path):
	user_table_path = path + '/user_table/' + username
	with open(user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		user['card_limit'] = user['card_limit'] + add_money
	with open(user_table_path, 'w', encoding='utf8') as wf:
		json.dump(user, wf)

def isAuth(func):
	def inner(username,path):

		res = func(username,path)
		#
	return inner


# def auth(sex = '女'):
# 	def isAuth(func):
# 		def inner(*x,**y):
# 			func(*x,**y)
# 			print(x)
# 			print(y)
# 			print(sex)
# 		return inner
# 	return isAuth

#认证用户
@isAuth  #AuthUser = isAuth(AuthUser)
def AuthUser(username,path):
	user_table_path = path + '/user_table/' + username
	with open(user_table_path, 'r', encoding='utf8') as rf:
		user = json.load(rf)
		user['auth'] = True
		user['card_num'] = user['username']+'12345678'
		user['card_limit'] = 10000
		user['total_card_limit'] = 10000
	with open(user_table_path, 'w', encoding='utf8') as wf:
		json.dump(user,wf)


if __name__ == '__main__':
	path = '/Users/sujunjun/PycharmProjects/fullstack_s2/review/atm_homework'
	#print(path + '/user_table/' + 'haha' + '.txt')
	#print(os.path.isfile(path + '/user_table/' + 'haha'))
	#rf = open(path, 'r', encoding='utf8')
	#user_info = json.load(rf)
	#print(user_info)
	#pass
	#AuthUser('haha',path)
	print(getUserAmount('haha',path))
	print(10 * 0.05)
	#freezeUser('haha',path)
