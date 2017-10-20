

'''
#2017   2027-2031
money=10000
for  year  in range(1,11):  #循环10年，每年递增
    money=money*1.05


money1=money  #每年增长
money2=money1*1.05
money3=money2*1.05
money4=money3*1.05


lastmoney=money1+money2+money3+money4 #四年叠加
print(lastmoney)
'''


'''
money=10000
for  year  in range(1,11):  #循环10年，每年递增
    money=money*1.05

lastmoney=money
for  year  in range(1,4):  #循环3次
    money=money*1.05
    lastmoney+=money

print(lastmoney)

'''

'''

money=10000
year=1
while  year<11:
    money=money*1.05
    year=year+1

lastmoney=money
year=1
while  year<4:
    money=money*1.05
    year=year+1
    lastmoney+=money


print(lastmoney)
'''

'''
money=10000
year=1
while  True:
    money=money*1.05
    year=year+1
    if year==10:
        break


lastmoney=money
year=1
while  True:
    money=money*1.05
    year=year+1
    lastmoney+=money
    if  year==4:
        break


print(lastmoney)
'''
'''
def add(num1,num2):
    return num1+num2

print(id(add))
print(type(add))
'''
'''
def  add(num1,num2):
    return num1+num2

def  sub(num1,num2):
    return num1-num2

def  getmax(num1,num2):  #业务的逻辑
   return num1 if num1>num2 else num2

def  Test(go,num1,num2): #接口，不变的，业务核心代码
    return go(num1,num2)

print(Test(add,1,2))
print(Test(sub,1,2))
print(Test(getmax,1,2))
'''

'''
def add(num1=1,num2=2):
    return num1+num2
print(add())   #，没有默认参数的情况下，调用函数无比正确传递参数
               #有默认值，可以不传
print(add(3)) #传递参数，从左往右填充
print(add(3,9)) #传递参数覆盖默认参数
'''
'''
def  getdata1():
    return 1

def  getdata2():
    return 1,2

def  getdata3():
    return 1,2,3


num1= getdata1()
print(num1)
num2,num3=getdata2()  #num2=1  num3=2
print(num2,num3)


def  getdata3():
    return 1,2,3
a,b,c=getdata3()
print(a,b,c)
'''
'''
#函数可以包含函数
#内层函数testin num覆盖外层  test  num，不同的变量，地址不一样

def  Test():
    num=10
    def Testin():
        num=100
        print("test in",num,id(num))

    Testin()
    print("test",num,id(num))

Test()


'''
#函数可以包含函数
#内层函数testin num覆盖外层  test  num，不同的变量，地址不一样


def  Test():
    num=10 #函数内部都是局部变量
    def Testin():
        nonlocal num #内层testin，直接操作外层Test，
        num=1000 #没有noloacal解释为新建一个变量，否则解释为重新赋值
        print("test in",num,id(num))

    Testin()
    print("test",num,id(num))

Test()











































