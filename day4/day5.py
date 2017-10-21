'''
password=input("请输入密码：")
while "123456"!=password:
    password=input("密码错误，请重新输入：")#循环体
print("密码正确")#循环跳出


while "123456"!=password:
    password=input("密码错误，请重新输入：")#循环体
else:
    print("密码正确")#循环终止条件

import turtle
#设定循环次数,包含了循环终止条件
#实现一个操作，常量
#常量修改变量
length=50 #初始
step=50  #每次加50
num=0   #循环10次，
while num<10:
    print(num)
    num+=1  #循环次数

    turtle.penup()
    turtle.goto(length, length)
    turtle.pendown()
    turtle.goto(length, -1 * length)
    turtle.goto(-1 * length, -1 * length)
    turtle.goto(-1 * length, length)
    turtle.goto(length, length)
    length+=step
else:
    print("out",num)
turtle.done()

import os

cmd=input("cmd")
while(cmd!="退出"):
    if cmd=="记事本":
        os.system("notepad")
    elif cmd=="进程":
        os.system("tasklist")
    else:
        os.system("echo  other")
    cmd=input("cmd")

while True:
    cmd = input("cmd")
    if cmd=="记事本":
        os.system("notepad")
    elif cmd=="进程":
        os.system("tasklist")
    elif cmd=="推出":
        break
    else:
        os.system("echo  other")


for i in range(1,200):
    print(i)




for i in range(0,200,2):
    print(i)
#for i in range(1,200):     100次，从0开始一直到99
#for i in range(0,200):     100次，从0开始一直到99
#for i in range(0,200，2):  100次，从0开始一直到99,每次步长为2

import time
#1，100000000  跑分

starttime=time.time() #开始时间
#跑分代码
lastnum=0
num=0  #1-》100000000
while num<100000000:
    num+=1
    lastnum+=num
print(lastnum)#最终数值
endtime=time.time()#结束时间
print(endtime-starttime)#时间差

#for  处理数据速度稍微快点
starttime=time.time() #开始时间
#跑分代码
lastnum=0
for  i  in  range(300000000):
    lastnum+=i
print(lastnum)#最终数值
endtime=time.time()#结束时间
print(endtime-starttime)#时间差


import time
import os


#每几秒操作一次
while True:
    time.sleep(5)
    os.system("notepad")


num=0
while True:
    time.sleep(1)
    print("第"+str(num)+"秒")
    num+=1


    if num==10:
        os.system("start notepad")
    elif num==20:
        os.system("taskkill /f /im notepad.exe")
    else:
        pass

for i in range(100):
    print(i)
else:
    print("OUT",i)
#不能处理死循环，不能处理实数。
# 所有的for循环都可以转化为while,而while转化为for着不一定


for  i  in range(8): #i循环一次，j循环5次
    for  j  in range(6): #50次
        print(j, end="  ")
    print("---------------", i)

import turtle
for  i  in  range(0,300,100):
    for j  in  range(0,400,100):
        turtle.goto(j,i)
        turtle.pendown()#跳过第一次
        turtle.write(str(i)+","+str(j))
    turtle.penup()

turtle.done()
'''
'''
num=eval(input("输入一个数字"))
for  i  in range(1000):
    if num==i:
        print("find")
        break  #break.中断循环，循环不再执行
    print(i)


for i  in range(100):
    if i==30:
        continue  #结束本次循环，本次循环contiune执行，后续本次循环后续代码不会执行
    print(i)

'''

'''
#筛选
for  i  in range(100):
    if i%2==1:
        continue
    print(i)

for  i  in range(100):
    if i%2==0:
        break
    print(i)
'''

'''
for  i  in  range(8):
    for j  in  range(10):
        print(j,end=" ")
        if j==5:
            break  #跳出j这个循环
    if i==5:
        break  #跳出i这个循环
    print("")
'''

for  i  in  range(8):
    if i == 5:#淘汰某一行
        continue
    for j  in  range(10):
        if j==5:  #淘汰某一列
            continue
        print(j, end=" ")

    print("")




























