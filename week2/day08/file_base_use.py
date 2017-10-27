#__author:  sujunjun
#date:  17/10/5
import time ,sys
#练习文件的操作
#实现三级菜单
#今天任务
#能调用方法的一定是对象
##三种基本的操作模式 r(只可读) w（只可写） a（追加）
#一般步骤:创建文件对象 --->调用文件方法操作 ------>关闭文件
#===========读
#file = open('1','r',encoding = 'utf8')#返回的是一个文件对象
#re = file.read(5) #可以指定要读几个字符
#file.write('哈哈哈哈') #注意这里会报错,读只能读,不能写
#print(re)
#file.close()


#===========写
# file = open('1','w',encoding = 'utf8')#<class '_io.TextIOWrapper'>
# #file.write('五星红旗我为你自豪')  #首先会做一个清空的操作,然后把你要写的内容写入文件中
# file.read()#这里会报错,因为写只能写不能再去读
# file.close()


#如果文件没有关闭,数据会被缓存下来,不会写入磁盘中
# file = open('1','w',encoding='utf8')
# file.write('开心快乐每一天')
# time.sleep(30)
# file.close()


#================具体的操作方法
#f = open('1','r',encoding='utf8')
# print(f.read(2))
# print(f.read(2)) #注意 ：汉字在这里占一个单位（in Py3）
# print(f.readline())
# print(f.readline())
# print(f.readline())#从光标位置开始读一行,无论是read还是readline/readdlines光标的位置都会发生变化,
# print(f.readlines())#返回一个列表,列表包含了文件的每一行内容,并且有换行符
# #['开心快乐每一天3\n', '开心快乐每一天4\n', '开心快乐每一天5\n', '开心快乐每一天6']
# f.close()


#=================通过循环逐行读取文件内容
# data = f.readlines()
#number = 0
# for i in data:
#     number += 1
#     if number == 5:
#         i = ''.join([i.strip(),'handle\n'])
#     print(i.strip())
# f.close()
##########对于大数据文件，要用以下方式（the best way）：
# number = 0
# for file_content in f:#解释:这是for内部将f做成一个迭代器,用一行取一行
#     number += 1
#     if number == 5:
#         file_content = ''.join([file_content.strip(),'handle\n'])#取代万恶的+
#     print(file_content.strip())
# f.close()

#=====基本操作
# print(f.tell())  #0 作用:获取当前光标所在位置 *
# print(f.read(2)) #开心
# print(f.tell()) #返回6  一个中文3个字节在utf8中
# print(f.read(2)) #快乐
# print(f.tell())  #12
# print(f.seek(0))  #移动光标到指定的位置 *
# print(f.tell())
# print(f.read(2))


#==========进度条的实例
#flush 作用把缓存里面的数据转移到磁盘上,可以用它做进度条
#sys.stdout 作用可以在终端上显示某个内容
#不加flush的时候:*并没有直接放入内存,而是放入缓冲区,暂时看不到,刷新完才能看,30个全放完结束了,一次性给用户看
#终端也是文件对象,
#
# for i in range(30):
#     sys.stdout.write("*") #如果不加flush,他是一个一个把*放入缓冲中,直到全部放完,他才把他们放入磁盘中
#     sys.stdout.flush()#进入缓冲区立刻更新,放一个更新一个,不等你全部放完
#     time.sleep(0.2)
# f.close()


#=======
# f = open('1','w',encoding='utf8')
# #truncate() 截断数据,不能再r模式下 ,默认不加参数是从开头一直截取
# #在w模式下：先清空，再写，再截断 (没有意义)
# #在a模式下：直接将指定位置后的内容截断
# f.truncate(9)#如果是中文的话默认3个字节,他会把前两个字符保留,之后的内容截断
# f.write('hello world')
# f.truncate(5)
# f.write('11hello world')
#
# f.close()

#======r+ w+ a+
#fileno 文件描述符,整数唯一

#a+ 光标默认在最后位置,开始写
#w+ 先清空，再写读
#f = open('1','r+',encoding='utf8')

#------验证r+模式
#r+ 光标默认在第0个位置,但是是在最后位置开始写
#f = open('1','r+',encoding='utf8')
#print(f.tell())
#print(f.readline())
# f.write('ccckk')

#------验证w+模式
#w+ 先清空，再写读
# f = open('1','w+',encoding='utf8')
# print(f.readline()) #因为先清空了,所以没有内容
# print(f.tell())# 0
# print(f.write('阿帕帕')) #开始写入
# print(f.tell())  #光标移动到了最后
# #print(f.seek(0)) #所以想看到就移动光标到开始位置
# print(f.readline()) #所以在读取还是没有

#------验证a+模式
#a+ 光标默认在最后位置,开始写
#f = open('1','a+',encoding='utf8')
#print(f.tell()) #217
#print(f.readline())#读不到,因为光标在最后
#f.write('ccckk')


#-----终极问题如何修改:只能采取重新创建一个文件的思路
#例子:将第5行最后面追加个hello
#方法一:
# f_read = open('1','r',encoding='utf8')
# f_write = open('2','w',encoding='utf8')
# num = 0;
# for i in f_read:
#     num +=1
#     if num == 5:
#         i = ''.join([i.strip(),'hello\n'])
#     f_write.write(i)
# f_read.close()
# f_write.close()

#方法二 with 方法 同时管理多个文件对象(推荐使用这种,不用我们手动关闭文件了)
num = 0;
with open('1','r',encoding='utf8') as r, open('2','w',encoding='utf8') as w :
    for i in r:
        num +=1
        if num == 5:
            i = ''.join([i.strip(),'hello_girl\n'])
        w.write(i)





















