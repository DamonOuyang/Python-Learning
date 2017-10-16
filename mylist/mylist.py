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






















