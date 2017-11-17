import socket,os

sk = socket.socket()
address = ('127.0.0.1',8002)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
talk_flag = False

while True:
	inp = input('>>>').strip() #post | 1.jpg  一会试一下input是否有空格
	cmd,path = inp.split('|')
	path = os.path.join(BASE_DIR,path)
	filename = os.path.basename(path)
	file_size = os.stat(path).st_size
	#一起打包传过去(还可能加目标位置)
	file_info = 'post|%s|%s'%(filename,file_size)
	sk.sendall(bytes(file_info,'utf8'))
	f =  open(path,'rb')#rb 是已bytes读bytes写
	has_sent= 0
	while has_sent != file_size: #判断是否上传完
		data = f.read(1024) #一段一段发 1024字节
		sk.sendall(data)
		has_sent += len(data)
	f.close()
	print('上传成功')

sk.close()






















