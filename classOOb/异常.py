
def add(num1,num2):
    assert (type(num1) != type(num2)),"gogogogogo" #静态断言，条件成立就不打印后面部分，条件不成立就打印后面的内容
    # print(num1+num2)

add(1,"2")

# def add(num1,num2):
#     assert (type(num1)==type(num2)),"gogogo" #静态断言
#     print(num1+num2)
# add(1,"2")

'''
def div(num,divnum):
    return num/divnum
print(div(10,0))
'''
'''
class 王建林:
    def __init__(self):
        self.name="王健林"
        self.mystr="先订一个小目标，赚它一个亿"
        self.money=20000000000000
class 王思聪(王建林):
    def __init__(self):
        super().__init__() # 调用王建林打下的根基
        self.name="王思聪"

china王建林=王建林()
china王思聪=王思聪()
print(china王建林.money)
print(china王建林.mystr)
print(china王建林.name)


print(china王思聪.name)
print(china王思聪.mystr)
print(china王思聪.money)
'''

'''
class Box:
    def __init__(self,x,y,z):
        if x > 10 or x < 2:
            raise 1
        if y>10 or y < 2:
            raise 2 # 报错，提示2，无法处理2
        if z>10 or z<2:
            raise 3
        self.x=x
        self.y=y
        self.z=z
try:
    b1 = Box(1, 4, 5)
except 1: #无法处理1
    print("1 error")
'''
'''
with open(r"E:\Python Learning\classOOb\2.txt","rb") as file:#这样写，就自动关闭文件
    for line in file:
        line=line.decode("gbk","ignore")
        print(line,end="")
'''

'''
#文件关闭了吗，没有关闭
for line  in open(r"E:\Python Learning\classOOb\2.txt","rb"): # 没有对象关闭文件
    line=line.decode("gbk","ignore")
    print(line,end="")
'''

'''
def makename(name):
    if name.find("SB") != -1:
        print(name)
        raise NameError #提示异常，程序没错，自己给别人报一个错
    print("OK")
    return name
# print(makename("SB"))

try:
    print(makename("SB1"))
except:
    print("error")
'''

'''
try:
    file=open(r"E:\Python Learning\classOOb\2.txt","rb")
    mystr=file.readline().decode("utf-8")
    mylist=mystr.split(" # ") # 返回一个list
    print(mylist)
    num=eval(mylist[0]) # 转化失败
    print(mystr,end="")
    print(num)
    # file.write("12321")
except FileNotFoundError:# 抛出一个异常，并列处理异常
    print("转化失败")
except NameError: # 特定的异常
    print("处理其他所有异常")
else: # 没有异常情况执行这个
    print("没有异常情况")

finally: # 有没有异常，无论如何都执行
    print("有没有异常，都执行这一句")
    file.close()
'''


'''
import pymysql
try:
    db=pymysql.connect("127.0.0.1","root","111111")
    db.close()
    print("密码关闭")
except pymysql.err.OperationalError: # 可以验证一个东西干好或者没干好。
    print("密码错误")
else: #用处理正确的结果
    print("没有错误的时候执行")
'''

# import pymysql  # 安装  pip  install  pymysql
# try:
#     db=pymysql.connect("127.0.0.1","root","111111")
#     db.close()
#     print("密码正确")
# except pymysql.err.OperationalError:  #可以验证一个东西干好或者没干好。
#     print("密码错误")
# else:
#     #用于处理正确的结果
#     print("没有错误的时候执行")

'''
num1=eval(input("num1:"))
num2=eval(input("num2:"))

try:
    print(num1/num2)
except ZeroDivisionError:
    print("num2禁止=0")

print("hello world")
'''
# print(1+"2")
# print(str(1)+2) # 一定出错的就是错误




























