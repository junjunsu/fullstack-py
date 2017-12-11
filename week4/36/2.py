#!/usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: 2.py 
@time: 2017/12/09
自己写的
"""
import psycopg2
import psycopg2.extras
# 数据库连接参数
conn = psycopg2.connect(database="broker", user="th3ash", password="Cjoek6973", host="47.95.28.159", port="5432")
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) #获取字典形式
# cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
# # insert one item
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (1, 'aaa'))
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))

cur.execute("SELECT * FROM ex_broker_info WHERE broker_uid < %s;", (77,))
#rows = cur.fetchall()      # all rows in table
rows = cur.fetchone()        # one rows in table
print(rows['gps_area'])
# for i in rows:
#     print(i)
conn.commit()
cur.close()
conn.close()
