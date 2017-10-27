import random
#print(help(random))
print(random.random())
print(random.randint(1,8)) #随机数字包括8
print(random.choice([1,2,[3,4],88,'aaa'])) #随机序列,字符串都可以
print(random.sample([1,2,[3,4],88,'aaa'],2)) #