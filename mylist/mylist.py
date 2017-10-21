'''
mylist=[x+1 for x in range(1,10)]
print(mylist)
print("----------------")
mylist=[x+1 for x in range(1,10,10)] #参数2 必须是被2整除的数
print(mylist)
print("----------------")
mylist=[x+1 for x in range(1,100,2) if x>=50] #列表表达式
print(mylist)

mylist=[[x,x-1,x*x] for x in range(10) if x>5]
print(mylist)
print("---------------------")
#嵌套循环
mylist=[[x,y] for x in range(10) if x<5 for y in range(10) if y<5]
print(mylist)
mylist=[ str([x,y]) for x in [1,2,3,4] for y in [6,7,8] ]
print(mylist)
print("---------------------")
# 生成一个矩阵函数
mylist=[]
for i in range(8):
    mylist.append([i*10+j for j in range(10)])

#这只是打印函数，没有其他的用途
for l in mylist:
    print(type(l))
    print(l)
'''
'''
import codecs
filepath=r"E:\Python Learning\大数据相关数据\1.txt"
file=codecs.open(filepath,"rb","gbk","ignore")#按照指定编码
mylist=file.readlines()#返回一个list,读取到内存中

savepath=r"E:\Python Learning\mylist\savepathtest.txt"
filegood=open(savepath,"wb")#打开一个文件，如果没有就创建，已有就打开

for line in  mylist:
    QQlist=line.split('----')
    if len(line)>50:
        #print(QQlist)
        filegood.write(line.encode("utf-8"))

file.close()
filegood.close()
'''
'''
import itertools
mylist=list(itertools.permutations(['A','B','C','D'],4)) # 排列
print(mylist)
print(len(mylist))

itertools.permutations([1,2,3,4],2)#排列，4个数的列表，取出3个数，不同的顺序算
print(type(mylist))
print(id(mylist))
'''
'''
import itertools
mylist=list(itertools.combinations(['A','B','C','D'],3))
print(mylist)
print(len(mylist))
'''

import itertools
mylist=["".join(x) for x in itertools.product("0123456789abcdefghijklmn",repeat=6)]
print(mylist)
print(len(mylist))
file=open("6pass.txt","wb")#生产数字密码
for i in mylist:
    file.write((i+"\r\n").encode("utf-8"))
file.close()

'''
import itertools
mylist=("".join(x) for x in itertools.product("0123456abc",repeat=2) )
print(mylist)# next(mylist) 生成一个破解一个 中括号为列表list,()小括号生成器
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
'''

class money:
    pass

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

Hello.存款(10)
Hello.取款(100)





















