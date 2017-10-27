#深浅拷贝
a = 1
b = 2
b = a
b = 'abd'
print(id(a))
print(id(b))


list1 = [[1,2,3],5,6]
#print(list1)
list2 = list1.copy()
#print(list2)
list2[1] = 'haha'
#print(list1)
#print(list2)
#浅拷贝只拷贝1层
list2[0][1] = 888
# print(list1)
# print(list2)
#浅拷贝场景 银行共享账号
import copy;
list3 = ['matianzi','1',[100,150]]
#list4 = copy.copy(list3) #作用等同于上一个
list4 = copy.deepcopy(list3)#深拷贝
list4[2][0] = 50
print(list3)
print(list4)



