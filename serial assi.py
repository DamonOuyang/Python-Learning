'''
num1=1
num2=2
print(num1,num2)
num1=num2=2  #连续赋值
print(num1,num2)
'''

num1,num2=1,2   # 等价于 num=1,num2=2 但是左右必须对称
print(num1,num2)

num1,num2,num3=1,2,3
# 等价于 num=1,num2=2 但是左右必须对称,叫做交互对称赋值
print(num1,num2)
