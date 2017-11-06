# 模拟实现一个ATM + 购物商城程序
#
# 额度 15000或自定义

# 实现购物商城，买东西加入 购物车，调用信用卡接口结账
# 可以提现，手续费5%
# 每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息(不做)--
# 支持多账户登录
# 支持账户间转账
# 记录每月日常消费流水
# 提供还款接口
# ATM记录操作日志

# 用户认证用装饰器


#(1) 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
import os ,sys, json
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,project_path)

from foo.user.handle_user import  addUser, AuthUser, subAccount, addAccount
from foo.shopping.shopping import  shoppingList
from foo.logger.logger import  recordLogger

#判断用户是否登录
#如果已经登录,那么直接进行首页,否则跳到登录界面
#注册



user_name = input('请输入用户名:')
password = input('请输入密码:')
res = addUser(str(user_name),str(password),project_path)
if res['error'] == True:
	print(res['msg'])
	exit()
#当前登录用户的信息
user_info = res['user_info']
#登录成功
#商品列表 #
shop_list = shoppingList()
goon_by = True
shopping_car_list = []
shop_account = 0
flag = True

for info in shop_list:
	print('序号:%d 商品名称:%s 价格:%s 剩余数量:%s' % (info['id'], info['shop_name'], info['price'], info['stock_num']))
while goon_by == True:
	shop_num = input('请选择你要购买的商品,不买了请输入n')
	for shop in shop_list:
		if shop_num == str(shop['id']):
			shopping_car_list.append(shop)
			shop_account += shop['price']
	if shop_num == 'n':
		break

# 记录日志



#只能使用信用卡支付,申请信用卡
auth = user_info.get('auth',False)
if auth == False:
	user_select = input("您当前还没有绑定信用卡,请进行认证 y/n")
	if user_select == 'y':
		AuthUser(user_info['username'],project_path)
	else:
		print("欢迎下次光临")
		exit()



# 进行结算:
current_account = user_info.get('card_limit',0)
if shop_account > current_account:
	#进行额度充值
	user_select = input("您当前额度不够,请进行充值 y/n")
	if user_select == 'y':
		pass
	else:
		print("欢迎下次光临")
		exit()

#最终结算:,扣款
user_submit = input("是否进行结算 y/n")
if user_submit == 'n':
	print("欢迎下次光临")
	exit()
sub_money = current_account - shop_account
subAccount(user_info['username'],sub_money,project_path) #扣款
print("结算成功,清单如下")
expend_log = {"expend_total_money":sub_money,"expend":shop_account}
logger = recordLogger(user_info['username'])
log = json.dumps(expend_log)
logger.info(log)






























