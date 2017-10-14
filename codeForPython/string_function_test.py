'''
str="hello python1"
print("-".join(str))
print(str.zfill(40))

print("hello")
'''
'''
print(type(print))
print(id(print))

def add(num1,num2,num3):
    return num1+num2+num3
print(type(add))
print(id(add))

'''
'''
import os
os.system("notepad")
print(type(os.system))
print(id(os.system))
'''
'''
mylist=[1,2,3,4,5,6,7]
print(type(mylist))
print(id(mylist))
print(mylist)
print("----------------")
mylist=[1,2,3,"abc",True]
print(id(mylist[0]))
print(id(mylist))
print(mylist)
mylist[0] = 100

print(id(mylist[0]))
print(id(mylist))
print(type(mylist))
print(mylist[0])
print(mylist)
'''
'''
mylist=[1,2,3,4,5,6,7]

for i in range(len(mylist)):
    print(mylist[i])

'''

'''    
        for i in mylist:
    print(mylist[i])
'''
'''
mylist=["122",2.6,3,4,5,6,7]
print(id(mylist))
for  i  in range(len(mylist)):#len(求长度)
    print(mylist[i],id(mylist[i]))#每个元素都有一个地址，元素是变量。
    if mylist[i] == 4:
        mylist[i]=400
    print(mylist[i],id(mylist[i]))
'''
'''
# Filename : test.py
# author by : www.w3cschool.cn

# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)

'''
'''
#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
'''
'''
data = {
    'no' : 1,
    'name' : 'W3CSchool',
    'url' : 'http://www.w3cschool.cn'
}
'''
'''

data = {
    "no" : 1,
    "name" : "W3CSchool",
    "url" : "http://www.w3cschool.cn"
}

json_str = json.dumps(data)
python_str = json.loads(json_str)
print ("Python 原始数据repr：", repr(data))
print ("JSON 对象          ：", json_str)
print ("Python 原始数据    ：", python_str)
'''
'''
myset={1,2,3,4,5,6}
myset.add(8)
myset.add(1)
print(myset)
print("---------")
myset=set("abcdefg")
myset.update("abcdxyz")#update 打碎字符串，插入，多个打碎后插入
print(myset)

myset={1,2,3,4,5,6}
myset.update([1,2,8,9])
print(myset)
myset.remove(5)
print(myset)

myset = {1,2,3,4,5,6}
for i in myset:
    print(i)
print(myset[0])
for idx,iddata in  enumerate(myset):
    print(idx,iddata)
'''
'''

#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()
'''
'''
mystack=[]
mystack.append(1)
print(mystack)
mystack.append(2)
print(mystack)
mystack.append(3)
print(mystack)
mystack.append(4)
print(mystack)
print(mystack.pop())
print(mystack)
print(mystack.pop())
print(mystack)
print(mystack.pop())
print(mystack)
'''
'''
import collections
queue=collections.deque([1,2,3,4,5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft())#获取要弹出的值，然后弹出,弹出左边的值
print(queue)
print(queue.pop()) #获取要弹出的值，然后弹出,弹出右边的值
print(queue)
'''
'''
from collections import deque # 数据结构集合
queue=deque([1,2,3,4,5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft())
print(queue)
'''










































































