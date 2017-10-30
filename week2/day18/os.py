import os
#是跟操作系统进行交互

print(os.getcwd()) #/Users/sujunjun/PycharmProjects/fullstack_s2 # 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir(r'/tmp') #改变当前工作目录
# print(os.getcwd())
# print(os.curdir) #返回当前目录  .
# print(os.pardir) #获取当前目录的父目录字符串名 ..

#os.makedirs('abc/alex')  # 可生成多层递归目录
#os.removedirs('abc/alex') #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 (只能删除空目录)
#os.mkdir('week2/day18/abd') #生成一个文件夹
#os.rmdir('week2/day18/abd')




#r 原生字符串,所有字符都不是转义字符,全是普通的字符串包括/n

# dirs = os.listdir('/Users/sujunjun/PycharmProjects/fullstack_s2') #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# #结果:['.git', '.idea', 'owner', 'review', 'week1', 'week2', 'wx', '小重山', '小重山1', '小重山2']
# print(dirs)

#os.remove('1') #删除一个文件,不能删除文件夹

#os.rename('小重山_1','小重山')  #重命名文件或目录

info = os.stat('./week1') #获取文件/目录信息 * #
#结果:os.stat_result(st_mode=16877, st_ino=20127742, st_dev=16777220, st_nlink=6, st_uid=501, st_gid=20, st_size=204, st_atime=1509245615, st_mtime=1508404369, st_ctime=1508404369)
#print(info.st_size)  #这个比较重要
#st_atime 是最后一次访问的时间
#st_mtime 修改文件时间

#print(os.sep)   #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"

print(os.linesep) #输出当前平台使用的行终止符
#windows \r\n 换行
#linux  \n   换行
#mac \r   #换行

#print(os.pathsep)  #windows  用; 作为分号.  mac/linux 下用:分隔符  #输出用于分割文件路径的字符串

#print(os.system('ls')) #使用shell命令

#print(os.environ) #获取系统环境变量

#print(os.path.abspath('./小重山'))  #返回path规范化的绝对路径
#print(os.path.split('/Users/sujunjun/PycharmProjects/fullstack_s2/小重山')) # 将path分割成目录和文件名二元组返回 ,其实就是找到最后一个斜杠进行分割

#print(os.path.dirname('/Users/sujunjun/PycharmProjects/fullstack_s2/小重山'))  #返回path的目录。其实就是os.path.split(path)的第一个元素
#print(os.path.dirname(os.path.dirname(__file__))) #拿到的是绝对路径 ,返回的是上一层的路径
#print(os.path.basename(__file__))  #拿到的是文件的名字 #os.py  #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
#print(__file__) #/Users/sujunjun/PycharmProjects/fullstack_s2/week2/day18/os.py

#print(os.path.join('Users','abc','bc')) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 #比如在abc前面加/,那么Users将被忽略

# os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False





