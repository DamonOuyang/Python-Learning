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

#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
'''
data = {
    'no' : 1,
    'name' : 'W3CSchool',
    'url' : 'http://www.w3cschool.cn'
}
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



















