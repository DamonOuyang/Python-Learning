'''
num
print(num)  #变量没有赋值，不可以引用
#NameError: name 'num' is not defined

str1="calc"
str2="calc"#地址赋值
print(id(str1),id(str2))
str1="calc1"#给变赋值，实际上传递新常量的地址
print(id(str1),id(str2))

num=10
num=None #None,是主要用于判断变量有没有人正在使用
print(num)
print(type(num))

a=5
print(a+1)#a+1 不会改变原来的值
print(a)
a=a+1#要改变原来的值，需要赋值
print(a)

doubledb=1024.88
print(int(doubledb))#临时变量
print(doubledb)

import turtle #画一个立方体

turtle.goto(200,0)
turtle.goto(200,200)
turtle.goto(0,200)
turtle.goto(0,0)

turtle.penup()
turtle.goto(110,110)
turtle.pendown()

turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(0,200)
turtle.goto(0,0)

turtle.done()


import  time #时间
mytimes = time.time()
print("自从1970现在过去了：",int(mytimes),"秒")
seconds=int(mytimes)%60 #秒
hours=int(mytimes)//3600 #过去了多少小时
mins=int(mytimes)-int(mytimes)//3600*3600#剩余的秒数
print("自从1970现在过去了：",
      hours,"小时",
      mins, "分",
      seconds, "秒")

#100%9=100-100//9*9=1
#3600+1550秒 = 5150秒
#1小时50秒
#5150-50-3600/60=

year=eval(input("请输入贷款年限："))
money=eval(input("请输入贷款金额："))
monthrate=eval(input("请输入贷款利率："))

monthmoney=(money*monthrate)/(1-1/(1+monthrate)**(year*12))
allmoney=monthmoney*12*year

print("月供：",monthmoney)
print("全部还款：",allmoney)


x1,y1,z1=eval(input("输入两个点的坐标："))#输入的时候，逗号分隔，连续输入3个数
print(x1,y1,z1)

x1,y1=eval(input("请输入x1,y1"))

print("1a"+"2b")
#print("1"+3)
'''

import math  #导入数学包
print(abs(-5))
print(abs(5))















