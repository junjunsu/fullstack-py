#str:unicode
#bytes:十六进制
#s = 'hello军哥'  #看到的数据类型是str , 存的是unicode编码 ,本身在内存里
#存入磁盘还是网络传输,都用bytes类型
#bytes类型离底层更近的,离二进制还差一步,计算机就能认识了
#bytes类型是0-255的数字

#由str 转到bytes这个叫编码
#bytes(s,'utf8') ->py提供的内置函数  第一个参数,你要转化的字符串,
#为什么转utf8
#各自有各自的编码规则 gbk ,utf8
#b = bytes('hello军哥','utf8')
#print(b) #b'hello\xe5\x86\x9b' 因为转的是assci表的内容跟utf8内容相同,所以hello会显示  ,而汉字占3个字节   ------>utf8规则下的bytes类型

#encode 编码 , decode解码
ss = 'hello军哥'
# b1 = ss.encode('utf8') #我要转的是bytes类型
# print(b1) #b'hello\xe5\x86\x9b\xe5\x93\xa5'  上下两个一样的



#bytes >>>>>>>>>>>>>str 解码
#错误的解码方式:
#b'hello\xe5\x86\x9b'  军  为什么写一个jun就报错,因为gbk是按2个字节代表一个汉字,多出来一个字节,所以报错
#b'hello\xe5\x86\x9b\xe5\x93\xa5'  军哥  为什么乱码因为gbk按2个字节代表一个汉字,数正好够6个字节,所以是乱码
#print(str(b1,'gbk')) #您本身按utf8规则编码是3个字节一个汉字,又用另外一个规则gbk解码,

#正确的:
#解码方法一:
#print(str(b1,'utf8')) #解码----str数据类型
#str数据类型没有(utf8,gbk) 因为它是万国码 ,只有bytes类型有按什么编码过来的

#解码方法2
#print(b1.decode('utf8'))




g1 = ss.encode('gbk') #gbk编码下的bytes数据
print(g1) #b'hello\xe5\x86\x9b\xe5\x93\xa5'    它用2字节个代表一个汉字

print(g1.decode('gbk')) #hello军哥










































