# _*_coding:gbk _*_

#__author:  sujunjun


# 二进制:
#
# ————>ASCII :只能存英文和拉丁字符,一个字符占一个字节,8位
# —————>gb2312:只能6700多个中文,  1980
# ————————->gbk1.0 :存了2万多字符,1995
# ——————————->gb18030:2000  ,27000中文
#
# ————————>unicode:utf-32 占4个字节
# ————————>unicode:utf-16 占2个字节或以上 65535
# ————————>unicode:utf8 一个中文占3个字节,用ascii保存

#date:  17/10/5
#py2  默认是ascii,写中文必须声明
#gbk默认不认识utf8,除非你文件编码按照gbk来,unicode向下兼容gbk
a = "特斯拉"
# 直接打印a SyntaxError: Non-ASCII character '\xe4' in file py2.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
print(a)
s_to_unicode = a.decode("gbk") #一定要写上之前我是什么编码 ,不写的话,默认用python默认的
unicode_to_utf8 = s_to_unicode.encode("utf-8")
#print("unicode:", s_to_unicode)
#print("gbk:", unicode_to_gbk)
#print(s_to_unicode) #特斯拉
#print(unicode_to_utf8)#特斯拉
#print("unicode:", s_to_unicode)#('unicode:', u'\u7279\u65af\u62c9')
#print("utf-8:", unicode_to_utf8)#('utf-8:', '\xe7\x89\xb9\xe6\x96\xaf\xe6\x8b\x89')

#utf8_to_unicode = unicode_to_utf8.encode("gbk") #不能直接转成gbk,
# 上面代码实际执行:unicode_to_utf8.decode().encode("gbk") 而你decode里面写的是ascii 所以报错
#Traceback (most recent call last):
#File "py2.py", line 32, in <module>
# utf8_to_unicode = unicode_to_utf8.encode("gbk") #??????????utf-8
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
#你应该
utf8_to_unicode = unicode_to_utf8.decode("utf-8")
unicode_to_gbk = utf8_to_unicode.encode("gbk")
print(utf8_to_unicode)
print(unicode_to_gbk)
#
# gbk_to_unicode = unicode_to_gbk.decode("gbk") #不能直接转成utf-8
# unicode_to_utf8 = gbk_to_unicode.encode("utf-8")
#
# print(gbk_to_unicode)
# print(unicode_to_utf8)


#py3
#in py3 默认unicode不需要任何的转码
#encode 在编码的同时,会把数据转化为bytes类型
#decode 在解码的同时,会把bytes类型转化成字符串
#b = byte = 字节类型 = [0-255]
# import sys
# print(sys.getdefaultencoding())
# a = "i am 特斯拉"
# a_to_gbk = a.encode("gbk")#在编码的同时,会把数据转化为bytes类型,如果想被看到(可读),只能在把他解回去
# print(a)
# print(a_to_gbk) # 输出:b'i am \xcc\xd8\xcb\xb9\xc0\xad'
# #b代表bytes类型.中文就会转成bytes,不同文件的传输也会用bytes(只能用),
#
# print(a_to_gbk.decode("gbk"))  #--------------这个就是 解回去的过程(转成unicode)
