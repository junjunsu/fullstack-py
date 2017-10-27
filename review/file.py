# f = open('小重山','r',encoding='utf8')#返回的是一个文件对象 需要指定路径,
# #res = f.read(2) #指定读几个字符
# res = f.readline()
# res = f.readlines()
# #res = '\n'.join(res)
# print(res)
import time,sys
# f = open('小重山','a',encoding='utf8')
# f.write('精忠报国111')



#time.sleep(20)
#f.close()

#========遍历
f = open('小重山','r',encoding='utf8')
# data = f.readlines()
# number = 0
# for i in data:
#     number += 1
#     if number == 5:
#         i = ''.join([i.strip(),'handle111\n'])
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
# print(f.tell())  #0 作用:获取当前光标所在位置 *
# print(f.read(2)) #开心
# print(f.tell()) #返回6  一个中文3个字节在utf8中
# print(f.read(2)) #快乐
# print(f.tell())  #12
# print(f.seek(0))  #移动光标到指定的位置 *
# print(f.tell())
# print(f.read(2))
#
#
# for i in range(30):
#     sys.stdout.write("*") #如果不加flush,他是一个一个把*放入缓冲中,直到全部放完,他才把他们放入磁盘中
#     sys.stdout.flush()#进入缓冲区立刻更新,放一个更新一个,不等你全部放完
#     time.sleep(0.2)
# f.close()

#r+ 光标默认在第0个位置,但是是在最后位置开始写
# f = open('小重山','r+',encoding='utf8')
# print(f.tell())
# #print(f.readline()) #25
# print(f.readlines()) #216
# print(f.tell())
# print(f.seek(0))
# f.write('马天资')

#w+ 先清空，再写读
# f = open('小重山','w+',encoding='utf8')
# #print(f.readline()) #因为先清空了,所以没有内容
# print(f.tell())# 0
# print(f.write('阿帕帕11')) #开始写入
# print(f.tell())  #光标移动到了最后
# print(f.seek(0)) #所以想看到就移动光标到开始位置
#print(f.readline()) #所以在读取还是没有

# num = 0;
# with open('小重山','r',encoding='utf8') as r, open('小重山1','w',encoding='utf8') as w :
#     for i in r:
#         num +=1
#         if num == 5:
#             i = ''.join([i.strip(),'hi美女\n'])
#         w.write(i)


#二进制模式
# f = open('小重山2','wb') #以二进制的形式读文件
# # f = open('小重山2','wb') #以二进制的形式写文件
# f.write('hello alvin!'.encode())#b'hello alvin!'就是一个二进制格式的数据,只是为了观看,没有显示成010101的形式

#rb模式
f = open('小重山','rb',) #以写读模式打开文件
print(f.tell())
f.seek(-1,2)
print(f.tell())
# print(f.read(3)) #b'\xe6\x98\xa8'
#
# #file.seek(off, whence=0)：从文件中移动off个操作标记（文件指针），正 往结束方向移动，负 往开始方向移动。如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。
# f.seek(3)
# print(f.read(3)) # b'\xe5\xa4\x9c'
#
# f.seek(3,1)
# print(f.read(3)) # b'\xe5\xaf\x92'
#
# f.seek(0)
# print(f.tell())
#print(f.read(3))   # b'\xe9\xb8\xa3'