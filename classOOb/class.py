'''
class Hello:
    a = 0
    b = 100
    _name=""
    _unm=""
    def __init__(self,num,name):
        self._unm = num
        self._name = name
    def 存款(self,num):
        self._unm+=num
        print(self._unm)
    def 取款(self,num):
        self._unm-=num
        print(self._unm)

# Hello.存款(10)
# Hello.取款(100)

hell = Hello(0,"Dimon")
hell.存款(1000)
hell.取款(200)

class MyClass:
    """一个简单的类实例"""
    def __init__(self):
        print("create")

    i = 12345

    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


#!/usr/bin/python3

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

# 实例化类
p = people('W3Cschool',10,30)
p.speak()

'''

'''
#!/usr/bin/python3

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student('ken',10,60,3)
s.speak()
'''
'''
# 多继承
#!/usr/bin/python3

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        # print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
        print("我叫 %s, 我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g) #初始化父类属性
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
'''
'''
class Parent: #定义父类
    def myMethod(self):
        print("调用父类方法")


class Child(Parent): #定义子类
    def myMethod(self):
        print("调用子类方法")

c = Child()  # 子类实例化
c.myMethod() # 子类调用重写方法

p = Parent()
p.myMethod()
'''
'''
#!/usr/bin/python3

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量
'''
'''
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d,%d)' %(self.a,self.b)


    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)

print(v1+v2)
'''
'''
import os
listdir  = dir(os)
# listhelp = help(os)
'''
'''
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""
To: jcaesar@example.org
From: soothsayer@example.org
...
... Beware the Ides of March.
... 
""")
server.quit()
'''
'''
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
'''
'''
def average(values):
    print(average([20, 30, 70]))
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试
'''
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
print(re.match('www', 'www.w3cschool.cn').span())  # 在起始位置匹配
print(re.match('com', 'www.w3cschool.cn'))         # 不在起始位置匹配
'''
'''
#!/usr/bin/python3
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
'''
'''
#!/usr/bin/python3

import re
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
'''
'''
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import re

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
'''














