#coding:utf-8
#print(['袁晗']) #['\xe8\xa2\x81\xe6\x99\x97'] 2.7


#2.7里面只有这两种数据类型
#str:bytes         str存的是bytes
# s = '袁浩hello'
# print len(s)  #11
# print repr(s)   #'\xe8\xa2\x81\xe6\xb5\xa9hello' 在内存中存的格式 hello在assci中有  ---存的是字节
# print type(s)    #<type 'str'>

#unicode:unicode    unicode存的是unicode
# s = u'袁浩hello'  #转化成unicode
# print repr(s)   #u'\u8881\u6d69hello'   ----存的是unicode
# print type(s)   #<type 'unicode'>
#
#
# print '原规划'#字节转成了unicode,但凡打印能看见明文的,它转成了unicode
# print 'yuan' + u'hao' #2.7做了转换,把bytes转换成了unicode
# print '元' + u'好' #两种数据类型拼接,只要脱离了assci码,它就不转换了,会报错
#总结:py2里面两种数据类型,他可以对assci里的内容进行拼接(bytes转换成了unicode),但是只要脱离了assci码,它就不转换了,会报错
#utf8数据转化成gbk -> utf8->unicode->gbk


#py3 里面还是2种数据类型 ,str bytes
#str存的是unicode,
#bytes存的是bytes

#3根2只是换了个名字吗?
#不是的,做了一个严格的区分bytes和str,bytes就是bytes,unicode就是unicode,str跟用户打交道,bytes是跟计算机打交道

#例子 py3中
#print(b'yuan'+'hao') #TypeError: can't concat bytes to str 进行了严格区分 bytes和unicode
print(type('str'))
import sys
A = '袁浩1a'
B = '袁浩2b'
C = '袁浩3c'
#sys.stdout.write(str(A) + '\n')
sys.stdout.write(' '.join(map(str, [A, B, C])) + '\n')
print A,B,C

























