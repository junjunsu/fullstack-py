#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: 1.py 
@time: 2017/12/09 
"""
import pymysql

# 创建连接
conn = pymysql.connect( host = '127.0.0.1', port = 3306, user = 'root', passwd = '123456', db = 'py' ,charset = 'utf8')
# 创建游标
#cursor = conn.cursor()
# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#更新
# 执行SQL，并返回收影响行数
#effect_row = cursor.execute( "update student set sname = %s where sid = %s",('小军',1,) ) #修改成功返回1修改失败返回0


#插入
# 执行SQL，并返回受影响行数
#effect_row = cursor.executemany("insert into student(gender,class_id,sname)values(%s,%s,%s)", [("男",4,'张晓军'),("女",4,'小花')]) #插入多条
#effect_row = cursor.execute("insert into student(gender,class_id,sname)values(%s,%s,%s)", ("女",4,'战天狗')) #插入一条
# 获取最新自增ID
#new_id = cursor.lastrowid   #如果是插入多条获取的是最后插入的那个id
#conn.commit()

#删除
#effect_row = cursor.execute("delete from student where sid = %s",(19,))

#查询
cursor.execute( "select * from student" )

# 获取第一行数据 (常用)
#row_1 = cursor.fetchone()#(1, '男', 1, '小军')  指针会下移
#row_1 = cursor.fetchone() #(3, '男', 1, '张三')
#row_1 = cursor.fetchone() #(3, '男', 1, '张三')

# 获取前n行数据
#row_2 = cursor.fetchmany(2) #这个不常用


# 获取所有数据(常用)
row_3 = cursor.fetchall()  #获取所有数据 默认以元组方式返回


print(row_3)


#注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
#row_1 = cursor.fetchone()#(1, '男', 1, '小军')  指针会下移
#row_1 = cursor.fetchone()#(2, '女', 1, '钢蛋')  指针会下移
#cursor.scroll(11,mode='absolute') # 绝对位置移动 指定移动多少位  从0开始,0是第一位
#cursor.scroll(-2,mode='relative')  # 相对当前位置移动  #正数向下移动,负数向上移动  从0开始,0是第一位  写1的话相当于相对当前位置向下移动2位
# row_1 = cursor.fetchone()#
#print(row_1)

# 提交，不然无法保存新建或者修改的数据

a = 123 if 1!=1 else 456 #三元运算
print(a)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
