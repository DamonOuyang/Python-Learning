'''
R = input("请输入圆形的半径")
print(R)
print(type(R))
R=eval(R)#字符串转化为实数
print(type(R))
print(R*R*3.1415926)

#运算符自动拆分换行
print(1+2+3+4+5+6+7+8+9+
      20+1+2+3+4+5+6+7+8+9+
      1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)
#一行写不下可以多行写


#用 \ 链接多行当作一行
print("lasdjldd dl \
      lsdd \
       alkds ")



num1=1;
num2=2;
num3=3;
print(num1,num2,num3)

num1=1
num2=2
num3=3
print(num1,num2,num3)

#多行归并一行，用分号分隔，最后一个不需要
num1=1;num2=2;num3=3;print(num1,num2,num3)

1 2 3
1 2 3
1 2 3

PI=3.1415926#PI只是规范起来，用于表示常量，实际是变量。
print(PI)
PI=123
print(PI)

num1=100
num2=15
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)#求实数
print(num1//num2)#//求整除
print(num1%num2)#求余数
print(num1**2)#求平方 num1*num1
print(num1**3)#求立方 num1*num1*num1
print(num1**0.5)#求开方根
print(num1**0.333)#求立方根

data=1.5e3 # 1.5*10^3
print(data)
data=1.5e-4 #1.5 /10/10/10/10
print(data)

data=100.8**1000000#错误 超过数字范围
print(data)

print((1+2)*3)#优先级
print(1+2-3+4)#结合性：优先级等同的情况下，从右往左，或则从左往右的运算

num=10
#num=num+1
num += 1 # 等价于num = num+1
#num + = 1 #错误，+= 必须连在一起
print(num)
num-=3
print(num)
num*=3
print(num)
#num/=2 # 整数整数结果实数，两个有一个是实数，结果总是实数
print(num)
num//=2#整数整数结果整数，两个有一个是实数，结果总是实数
print(num)
num %=5
print(num)
num **=3 #num=num**3
print(num)


num=3
print(type(num))

num=str(num)#str（要转换为字符串的数据）
print(type(num))
#eval 字符串转数字
num=4.5
print(int(num))#int(取整数)


num=10.56
print(round(num))


#10.84
#11.83
#提取出最后一个数
#10.84*10=108.4-108=0.4/10=0.04
data=eval(input("输入RMB"))
print(  (  data*10 - ( int(data*10) )  ) /10 )

'''

import time  #时间
timedata=time.time()
timedata=int(timedata)#取整数，多少秒

#print(timedata/1000)
print(timedata/3600)#小时
print(timedata/3600/24)#天
print(timedata/3600/24/365)#年

print(timedata%60)














