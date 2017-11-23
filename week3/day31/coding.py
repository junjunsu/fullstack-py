#coding:utf-8

import json
# s = '袁浩'
# b1 = s.encode('utf8')
# print(b1,type(b1))
# print(b1.decode('utf8'))
# print(b1.decode('gbk'))
#
#
# #
# b2 = s.encode('gbk')
# print(b2,type(b2))
# print(b2.decode('gbk'))
# #print(b2.decode('utf8'))#位数不够所以报错 utf8需要6个字节总共
# print(json.dumps(s)) #"\u8881\u6d69" 实在想看unicode就用这种在3中 ,2中用repr



#第二种
# s = '袁浩'
# b = bytes(s,'utf8')
# print(b)
#
# ss = str(b,'utf8')
# print(ss)

print (['袁浩']) #['\xe8\xa2\x81\xe6\xb5\xa9'] 为什么显示bytes
#这个跟print有关系

#打开文件那个为什么linux下不写那个encoding,windows必须要加,为什么改成gbk就可以了

