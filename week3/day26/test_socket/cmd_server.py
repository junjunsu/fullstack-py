#传送命令对方执行
#我这边发一个命令,你那边执行了,把结果给我看


import socket,subprocess
#popen是一个类, ,stdout=subprocess.PIPE
#2个参数有结果
#obj = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE) #windows上没有shell = True不行
#他在这里其实是自己开了一个进程,这个进程跟主进程没关系的,现在他有自己的一块区域,,他们两个并行执行,print(a)跟你这里面执行命令的结果是并行往下走的谁快谁先打印
#这不叫并行这叫多进程,相当于有了一个自己的子进程
#obj.stdout.read()
#print(str(obj.stdout.read(),'utf8')) #问题是这个结果直接显示屏幕上了,我想要付给一个变量传输用,其实这个结果是在他自己的一个子进程里面了,通过一个方法从他的子进程里面挪到我的主进程里面
#所以通过 管道 stdout=subprocess.PIPE  这就相当于把标准输出通过管道(PIPE)由子进程转到主进程里面(PIPE相当于管道),,他在子进程显示出来的,加上subprocess.PIPE之后通过管道封装到
#对象里面去




sk = socket.socket()
address = ('127.0.0.1',8001)
sk.bind(address)
sk.listen(3)

print('waiting........')
while 1:
	conn, addr = sk.accept()
	while 1:
		try:

			data = conn.recv(1024)
		except Exception:
			break
		if not data:break
		print('.........',str(data,'utf8'))
		#obj = subprocess.Popen(str(data,'utf8'),shell=True,stdout= subprocess.PIPE) #上下解码都可以
		obj = subprocess.Popen(data.decode('utf8'),shell=True,stdout= subprocess.PIPE)
		cmd_result = obj.stdout.read()  # cmd_result是bytes类型,是上面语句做的,他是按一个规则转化成的bytes, windows执行这个命令下默认用gbk,转成bytes
		result_len = bytes(str(len(cmd_result)),'utf8') #bytes转int转不了 , 只能先转成字符串
		print('>>>>>>>>>>',result_len)
		conn.sendall(result_len) #内容少会等待一下,

		conn.recv(1024) #解决粘包

		conn.sendall(cmd_result)
sk.close()

#粘包现象:2个send在一起有可能造成粘包现象,解决办法,s端加一个recv c端加一个sendall
#加sleep 很low 长了影响效率






























