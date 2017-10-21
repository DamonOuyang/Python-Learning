'''
import turtle
turtle.screensize(3024,2768)#屏幕
turtle.write("hello天朝",font=("华文琥珀",20,"normal"))#设定字体大小
turtle.showturtle()#显示
turtle.circle(100,steps=10)
turtle.done()

wangtao="天才"
if wangtao=="天才": #判断成立,执行或者不成立,不执行。
    print("天才的成才")#python中间的空格起到代码块分隔作用
print("hello world")



import os
cmd=input("cmd:")
if  cmd=="notepad":
    os.system("notepad")

import os
cmd=input("cmd:")
isRun=(cmd=="notepad")#cmd=="notepad" 逻辑表达式，返回真，返回假
print(isRun)
if  isRun:
    os.system("notepad")

王涛的颜值=98
王涛的女神期望值=93
print(王涛的颜值 >= 王涛的女神期望值)
if 王涛的颜值 >= 王涛的女神期望值:#关系运算符，#在日常生活中，没有回答是一种回答。
    print("王涛的女神嫁给王涛")


#字符串也可以比较大小，主要用在文件的排序。
bt1="ab备胎"
bt2="ac备胎"
bt3="aa备胎" # 第一个相等比第二个，第二个相等比第三个... 按照比较ASCII码比较
print(bt1 != bt2)#判断字符串不等
print(bt1 == bt2)#判断字符串相等
print(bt1 > bt2)
print(bt1 < bt2)
print(bt1 > bt2)
print(bt1 < bt2)
# print(bt1 > bt2)

print(ord("0"))
print(ord("a"))
print(ord("b"))
print(ord("z"))

print(int(True))#  1 , true
print(int(False))# 0 , false
print(bool(4))
print(bool(1))# 0为false,非0为 true
print(bool(0))
print(bool(-1))
print("str",bool(""))# 字符为空 false
print("str",bool("1"))# 字符为非空true
#if 语句会把这样的类型转化为 bool 类型

if -1:
    print("hello python1")
if "": # if 自动转化为 bool 类型
    print("hello python2")
if " ": # if 自动转化为 bool 类型
    print("hello python3")
if None: # if 自动转化为 bool 类型, bool(None)=false
    print("hello python3")

import random
num1 = random.randint(0,13)
num2 = random.randint(0,13)#生成10-100的随机数，包含0，包含100

num3 = random.randrange(0,10);#生成0-10的随机数，不包含10
print("小宝宝  %d + %d "%(num1,num2))# % 映射
print("小宝宝2  %d "%(num3))# % 映射
num = input("baby input:")
num = eval(num)
if num == num1+num2:
    print("小宝宝好聪明")

Dimon ,食人国国王
1 说真话，砍头  我被绞死
2 说假话，绞死  我被绞死

if(真话)
    砍头
if(假话)
    绞死
if(真话)
    砍头
else :
    绞死

if 0:
    print("hello python")
else:
    print("hello html5")


M颜值=10000
M身高=10000
RMB身高=10000

M颜值2=10000
M身高2=10000
RMB身高2=10000

ismarry1 = (M颜值   > M颜值2)
ismarry2 = (M身高   > M身高2)
ismarry3 = (RMB身高 > RMB身高2)

if ismarry1 and ismarry2 and ismarry3:
    print("-------------")
else:
    print("xxxxxxxxxxxxx")


M颜值=10000
M身高=10000
RMB身高=10000

M颜值2=10000
M身高2=10000
RMB身高2=10000

ismarry1 = (M颜值   > M颜值2)
ismarry2 = (M身高   > M身高2)
ismarry3 = (RMB身高 > RMB身高2)

if ismarry1 or ismarry2 or ismarry3:
    print("-------------")
else:
    print("xxxxxxxxxxxxx")# or 有一个满足即可，全部不满足才会淘汰


sex=True
if not not not sex:#not结合性，从右往左
    print("boy")
else:
    print("girl")
#not True=false
#not false=True
#not结合性，从右往左

print(3>2 and 10)#与运算符，没有找到假之前，都取最后成立的值。
print(bool(3<2 and 10))#短路，有一个不符合，后续不再判断
print(2<3 or 10)#或运算符，没有找到真之前，都成立取最后的值。

num1=3
num2=3
print(id(num1))
print(id(num2))
if num1 is num2:# is 身份运算符
    print("同一个地址")

#num1=4
if num1 is num2:# is 身份运算符
    print("同一个地址")
else:
    print("不同一个地址")

#num1=4
if num1 is not num2:# is not 身份运算符
    print("不同一个地址")
else:
    print("同一个地址")


print(1+2*2/3>2*(3-2)+1)
# 1+1.3333>2+1
# 2.333>3
# +3 > -2 # 表示正负 （一元运算符，一个操作数）
# 3-2 ，2+3 表示加减法（二元运算符，两个操作数）
print(   (1+2*2/3)  >  (2*(3-2)+1)  )#软件工程规范
print(1<2)#true 1
print(1<2>0)#1>0   true #2<0  true
print(1<2)  #1<0   false#2<0  false

# x 关系 y 关系 z 等价 x 关系 y 且 y 关系 z
print(5>3)# true 1 # python 中的一个特例
print(5>3>2)# 5>3 && 3>2   1>2
print(5>3<2)# 5>3 && 3<2   1<2

#pass
#pass # 空语句，什么都不执行
import os
cmd=input("请输入指令:")
if cmd == "关机":
    os.system("shutdown -s -t 200")
else:
    pass # 表示空语句，占位作用
print("game over")


mystr=input("妹子的潜台词")
if mystr=="我不想破坏我们之间的友谊":
    print("我们之间仅仅会有友谊")
elif mystr=="你真是一个好人":
    print("我们之间仅仅会有友谊")
elif mystr=="你真是一个好人":
    print("我们之间仅仅会有友谊")
elif mystr=="你真是一个好人":
    print("我们之间仅仅会有友谊")
elif mystr=="你真是一个好人":
    print("我们之间仅仅会有友谊")
elif mystr=="我还没有勇气接受你":
    print("看到你差点没被吓死，还敢接受你")
elif mystr=="我们还是做朋友好了":
    print("你还有利用价值，有义务，没权利")
elif mystr=="我们还是做朋友好了":
    print("你还有利用价值，有义务，没权利")
elif mystr=="我还小":
    print("你做我备胎，等我找不到再说")
else :
    print("没有回答是一种回答")

cmd = None
cmd = 1# 判断一个变量有没有被使用
if cmd:
    print("有对象")
else:
    print("没有对象")

import os
cmdstr=input("输入命令：")
if cmdstr=="记事本":
    os.system("notepad")
elif cmdstr=="计算器":
    os.system("calc")
elif cmdstr=="进程":
    os.system("tasklist")
elif cmdstr=="IP地址":
    os.system("ipconfig")
elif cmdstr=="重启":
    os.system("shutdown -r -t 200")
elif cmdstr=="关机":
    os.system("shutdown -s -t 200")
else:
    print("其它命令还没有翻译")

name=input("please input name:")
age=eval(input("please input age:"))
tall=eval(input("please input tall:"))
star=eval(input("please input star:"))
pos=eval(input("please input pos:"))
# XX  北京，年龄，身高，星座
if pos!="北京":
    print("地址不符合，淘汰")
else:
    if age <= 40:
        print("age不符合，淘汰")
    else:
        if tall <= 170:
            print("age不符合，淘汰")
        else:
            if star == "摩羯座":
                print("star 不符合，淘汰")
            else:
                print("符合符合:",name)


score = input("高考分数")
score = eval(score)
if score>750:
    print("输入错误!")
else:
    if score<0:
        print("输入错误!")
    else:
        if score >= 700 and score<=750:
            print("清北")
        else:
            if score>=600 and score<700:
                print("985")
            else:
                if score >= 550 and score<600:
                    print("211")
                else:
                    if score >= 550 and score < 580:
                        print("1本")
                    else:
                        if score >= 500 and score < 550:
                            print("2本")
                        else:
                            if score < 500 and score < 450:
                                print("2本")
                            else:
                                print("大专")

score = input("高考分数")
score = eval(score)
if score>750 and score<0:
    print("输入错误!")
elif score>600:  # 进这里，就不进下面的条件了 顺序很严格。不顺序，会产生误差
    print("清北")
elif score>700:  # 进上面，就不进这里了
    print("清北")
elif score>300:
    print("清北")
else:
    print("清北")

import turtle
x1,y2 = eval(input("圆心:"))
turtle.write(str(x1)+","+str(y2))
turtle.goto(x1,y2)
turtle.circle(100)

turtle.done()

import turtle
R=100
x1,y1=eval(input("圆心"))
turtle.write(str(x1)+","+str(y1))
turtle.penup()
turtle.goto(x1,y1-R) #移动圆心
turtle.pendown()
turtle.circle(R)

x2,y2=eval(input("pos"))
turtle.penup()
turtle.goto(x2,y2) #移动到输入的位置
turtle.pendown()
turtle.dot(10,"red")#绘制点，颜色红色
turtle.goto(x1,y1)#连线
length= ((x1-x2)**2+(y1-y2)**2)**0.5
print(length)
if  length==R:
    print("圆上")
elif  length <R:
    print("圆内")
else:
    print("园外")

turtle.done()

'''



























































