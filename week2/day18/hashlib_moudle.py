import hashlib
# m = hashlib.md5()  #<md5 HASH object @ 0x1085a83a0>
# m.update('hello world'.encode('utf8'))
# #在py3 存的都是unicode     需要转化成字节类型 bytes
# print(m.hexdigest()) #5eb63bbbe01eeed093cb22bb8f5acdc3  #转化的结果
#
# m.update('alex'.encode('utf8'))  #其实上下就是hello worldalex
# print(m.hexdigest()) #82bb8a99b05a2d8b0de2ed691576341a
#
#
# m2 = hashlib.md5()
# m2.update('hello worldalex'.encode('utf8'))  #上面的其实就是这种转化,上下结果一样的
# print(m.hexdigest()) #82bb8a99b05a2d8b0de2ed691576341a


#更高级的算法
# s = hashlib.sha256()#这个比较常用
# s.update('hello world'.encode('utf8'))
# print(s.hexdigest()) #b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9

import hmac
#它内部对我们创建 key 和 内容 再进行处理然后再加密:
h = hmac.new('alvin'.encode('utf8'))
h.update('hello'.encode('utf8'))
print (h.hexdigest())#320df9832eab4c038b6c1d7ed73a5940


