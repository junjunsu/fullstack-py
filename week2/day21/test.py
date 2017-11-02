#-*-coding:utf-8-*-

#dic = {""}
# dic1 = str({"name":"xoa"})
# f = open('test','w')
# f.write(dic1) #TypeError: write() argument must be str, not set

f = open('test','r')
data = f.read()
print(eval(data)['name']) #转回字典