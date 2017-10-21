'''
import  win32com.client# 系统客户端包
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#系统接口
speaker.Speaker("我是凤姐")

import  win32com.client# 系统客户端包
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#系统接口
#while,规则，与if一样，会对表示式进行转换
#True,1，2，-1，“ ”，True,1.234 继续循环
#false, 0,"",None,False 退出循环
while True:
    speaker.Speaker("我是凤姐")

import  win32com.client# 系统客户端包
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#系统接口
i=0
while i<5: # 有限循环
    print(i)
    speaker.Speaker("我是凤姐,这是第"+str(i+1)+"次")
    i+=1
else:
    speaker.Speaker("我是凤姐,我烦了")
    print("go",i)

import  win32com.client# 系统客户端包
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#系统接口
num=0
while num<7:
    print("while",num)
    speaker.Speak("吴东的女神有"+str(num)+"个备胎")
    num += 1
else:
    print("else",num)
    speaker.Speak("吴东的女神有" + str(num) + "个备胎，够了忙不过来")

import time
num=2.0
while num!=0: # 会出现无限循环,实数存在不精确，浮点数存在误差
    num -= 0.1
    print(num)
    time.sleep(0.5)

import time
num=2.0
# num - 0 <= 0.000001 # -6.38378239159465e-16=-0.00(16个0)638
while num-0>0.000000001:#folat 浮点数的误差，主要用于金融
    num -= 0.1
    print(num)
    time.sleep(0.5)


num=5
print("hello " if num>5 else"world")
#if bool() -> true AAAAA  if bool() -> false BBBBB
print("AAAA " if bool(3) else "BBBBB")

x=10
num=10 if x>8 else 5
print(num)


ages=20
price = 20 if ages>=16 else 10
print(price)


import  os
os.system("calc") if 3>0 else os.system("notepad")


#赌博概率 概率论
#1-10
import random
num=random.randint(1,100)
print("输了" if num<52 else "赢了")#澳门赌博的概率
#100  80

#一元二次方程
#先分类，把框架搭起来，再写代码
a,b,c=eval(input("a,b,c:"))
if a==0:
    if b==0:
        if c==0:
            print("x等于任意值")
        else:
            print("无解")
    else:
        print("x=",-1*c/b)
else:
    dt=b*b-4*a*c
    if dt==0:
        print("x1=x2=", -1 * b / 2 / a)
    elif dt > 0:
        print("x1=",(-b+dt**0.5)/(2*a), ",x2=",(-b-dt**0.5)/(2*a))
    else:
        print("x1=", -1 * b / 2 / a, "+", (-1 * dt) ** 0.5 / (2 * a), "i")
        print("x2=", -1 * b / 2 / a, "-", (-1 * dt) ** 0.5 / (2 * a), "i")

a,b,c=eval(input("a,b,c:"))
if a>b:
    if a>c:
        print("max:",a)
        if b>c:
            print(b,c)
        else:
            print(c, b)
    else:
        print("max:", c)
        if c>a:
            print(c,a)
        else:
            print(a, c)
else:
    if b>c:
        print("max:",b)
        if b>c:
            print(c,b)
        else:
            print(c, b)
    else:
        print("max:", c)
        if b>a:
            print(b,a)
        else:
            print(a, b)

year=eval(input("year"))
month=eval(input("month"))
if month==1:
    print(31)
elif month==2:
    if year%4==0 and year%100!=0:
        print(29)
    elif year%4==0 and year%400==0 and year%100==0:
        print(29)
    else:
        print(28)
elif month==3:
    print(30)
elif month==4:
    print(31)
elif month==5:
    print(30)
elif month==6:
    print(31)
elif month==7:
    print(30)
elif month==8:
    print(31)
elif month==9:
    print(30)
elif month==10:
    print(31)
elif month==11:
    print(30)
elif month==12:
    print(31)
else:
    print("脑子进水了")

import turtle
import math

turtle.penup()
turtle.goto(200,100)
turtle.pendown()

turtle.goto(200,-100)
turtle.goto(-200,-100)
turtle.goto(-200,100)
turtle.goto(200,100)

x,y=eval(input("input pos x,y:"))
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.dot(6,"red")
x=abs(x)
y=abs(y)
if x<200 and y<100:
    print("矩形内部")
elif x==200 and y<=100:
    print("矩形高度边上")
elif x == 100 or y <= 200:
    print("矩形宽度边上")
else:
    print("在矩形外部")

turtle.done()

import random
data=random.randint(1,13)
change=random.randint(1,4)
if change==1:
    print("红桃")
elif change==2:
    print("黑桃")
elif change==3:
    print("方块")
else:
    print("梅花")

if data==1:
    print("A")
elif data==2:
    print("2")
elif data==3:
    print("3")
elif data==4:
    print("4")
elif data==5:
    print("5")
elif data==6:
    print("6")
elif data==7:
    print("7")
elif data==8:
    print("8")
elif data==9:
    print("9")
elif data==10:
    print("10")
elif data==11:
    print("J")
elif data==12:
    print("Q")
elif data==13:
    print("K")


num=eval(input("输入三位整数:"))#100,999
if (num//100>0 and num//100<10):
    print("三位数")
    b=num//100 #百位
    c=num%10   #个位
    if b==c:
        print("是回文数")
    else:
        print("不是回文数")
else:
    print("不是三位数")

num=eval(input("输入数据0-15:"))
if num<0 or num > 15:
    print("输入错误")
else:
    if num>=1 and num <=9:
        print(num)
    elif num==10:
        print("A")
    elif num == 11:
        print("B")
    elif num == 12:
        print("C")
    elif num == 13:
        print("D")
    elif num == 14:
        print("E")
    elif num == 15:
        print("F")

num=eval(input("输入数据:"))#100,999
if num<0 or num >15:
    print("输入错误！")
else:
    if num >= 1 and num <= 9:
        print(num)
    else:
        print(chr(ord('A')+num-10))#字符转化


num=input("input 16 hex:")
if num=="a" or num=='A':
    print(10)
elif num=="b" or num=='B':
    print(11)
elif num=="c" or num=='C':
    print(12)
elif num=="d" or num=='D':
    print(13)
elif num=="e" or num=='E':
    print(14)
elif num=="f" or num=='F':
    print(15)
elif eval(num)>=0 or eval(num)<=9:
    print(eval(num))
else:
    print("error")


import os
while True:
    cmd=input("指令：")
    if cmd=="记事本":
        os.system("notepad")
    elif cmd=="计算器":
        os.system("calc")
    else:
        print("其它指令有待输入")


#13x+8y=200
#5,3,0.333
#1   7*13=91
#y=(100-13*x)//8
#13*4+6*8=52+48=100

# 15x+10y=1000

x=0
while x <= (100//13):
    if (100-13*x)%8==0:
        print("x",x,"y",(100-13*x)//8)
    x=x+1


#15x+10y=1000
#x=(1000-10*y)//15
y=0
while y<=1000//10:
    if (1000-10*y)%15==0:
        print("x",(1000-10*y)//15,"y",y)
    y+=1


import os
import time
while -1:
    #os.system("notepad")#同步模式，一个程序执行结束，再执行下一个
    os.system("start notepad")
    time.sleep(1)#1秒暂停
'''
import win32process #进程模块
import win32con#系统定义
import win32api#调用系统模块
import ctypes#C语言类型
import win32gui #界面

#一个常量，标识最高权限打开一个进程
PROCESS_ALL_ACCESS=(0x000F0000|0x00100000|0xFFF) # |位运算，0x十六进制
window=win32gui.FindWindow("MainWindow","植物大战僵尸中文版")#查找窗体
hid,pid=win32process.GetWindowThreadProcessId(window) #根据窗体抓取进程编号
phand=win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)#用最高权限打开进程编号
date=ctypes.c_long()#C语言的整数类型，读取数据
#加载内核模块
mydll=ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32.dll")

#读取内存，  int(phand)打开的进程编号  244866760,内存地址， 写入结果ctypes.byref(date)
#整数4个字节
mydll.ReadProcessMemory(int(phand),244866760,ctypes.byref(date),4,None)#读取内存
print(date.value)
newdata=ctypes.c_long(2048)#设定修改数据为2048
mydll.WriteProcessMemory(int(phand),244866760,  ctypes.byref(newdata),4,None )





































































