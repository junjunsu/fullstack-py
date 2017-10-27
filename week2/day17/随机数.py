#-*-coding:utf-8-*-
import random
print(random.random())
print(random.randint(1,8)) #包含8
print(random.randrange(1,3))  #这种情况多(不包含3)
print(random.choice([1,2,[4,5],'haha']))
print(random.choice('hello'))
print(random.sample([[1,2],[4,5],7,8],2))  #第二个参数可以指定随机的数目



add = random.choice([random.randrange(10),random.randrange(65,91)]);
#print(add)
code = ''
for i in range(5):
    add = random.choice([random.randrange(10),chr(random.randrange(65,91))])
    code+=str(add)

print(code)
