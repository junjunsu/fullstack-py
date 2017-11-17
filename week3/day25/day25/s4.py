#__author:  Administrator
#date:  2016/9/23
"""
class Tearch:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.salary = 1000

class Course:

    def __init__(self, name, cost, tearcher):
        self.name = name
        self.tearcher = tearcher
        self.cost = cost

    def class_up(self):
        self.tearcher.salary += self.cost



t1 = Tearch('李杰' ,8)
t2 = Tearch('烧饼', 9)
t3 = Tearch('豆饼', 10)

c1 = Course('生理课', 1, t1)

print(c1.name)
print(c1.tearcher.age)
print(c1.tearcher.name)
print(c1.tearcher.salary)

c1.class_up()

print(c1.tearcher.salary)
"""

class F1:

    def __init__(self):
        self.name = 123

class F2:

    def __init__(self, a):
        self.ff = a # [name=123]

class F3:

    def __init__(self, b):
        self.dd = b

f1 = F1()  # [name=123]
f2 = F2(f1)# [ff=[name=123]]
f3 = F3(f2) # [dd=[ff=[name=123]]]
# 找到123并输出
print(f3.dd.ff.name)




# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、上海 2 所学校
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校，




# 6. 提供两个角色接口
# 6.1 学员视图， 可以注册， 交学费， 选择班级，  (用户--学生)
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 (用户--老师)
# 6.3 管理视图，创建讲师， 创建班级，创建课程(管理员)
#
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里  (dump )

