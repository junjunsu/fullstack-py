import logging
#记录ATM操作日志

def recordLogger(username):
	logger = logging.getLogger()  # 拿到一个logger对象  #默认logger对象没有文件输出和屏幕输出对象,所以需要创建
	logger.setLevel(logging.DEBUG)  # 设置级别
	# 创建一个handler，用于写入日志文件
	fh = logging.FileHandler(username+'.log')  # 创建一个文件对象 #应该是一个路径加文件名,我不写是创建到当前工作路径下

	# 再创建一个handler，用于输出到控制台
	ch = logging.StreamHandler()  # 屏幕对象

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 格式对象

	fh.setFormatter(formatter)  # 文件对象格式
	ch.setFormatter(formatter)  # 屏幕对象格式

	logger.addHandler(fh)  # logger对象可以添加多个fh和ch对象
	logger.addHandler(ch)
	return logger

def recordATM():
	pass

#记录每月日日常流水
def recordOverhead():
	pass

def withdrawMoney():
	pass

if __name__ == '__main__':
	logger = recordLogger()
	logger.error({"name":10,"age":20})
