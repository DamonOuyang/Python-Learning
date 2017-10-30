import os
from collections import deque


path=r"E:\Python Learning\classOOb"
queue=deque([]) # 一个空的队列
queue.append(path) #把当前遍历的文件夹入栈

while len(queue)!=0:
    path=queue.popleft()#取出路径与层次
    filelist=os.listdir(path)#遍历路径

    for filename in filelist:
        filepath = os.path.join(path, filename)

        if os.path.isdir(filepath):
            print("文件夹", filename)
            queue.append(filepath)
        else:
            print("文件", filename)








'''
# 栈模拟递归实现文件夹有层次感
import os
path=r"E:\Python Learning\classOOb"
mystack=[]
mystack.append([path,0]) #把当前遍历的文件夹入栈

while len(mystack)!=0:
    pathlist=mystack.pop()#取出路径与层次
    filelist=os.listdir(pathlist[0])#遍历路径

    num=pathlist[1] # 代表层次
    headstr=""
    for i in range(num): # 控制层次感
        headstr+="  "

    #for filename in filelist:
    for i in range(len(filelist)):
        filename=filelist[len(filelist)-1-i]
        filepath=os.path.join(pathlist[0],filename)#链接,取得绝对路径
        if os.path.isdir(filepath): # 是文件夹
            print(headstr,"文件夹",filepath)
            mystack.append([filepath,num+1])
        else: # 是文件
            print(headstr,"文件",filepath)
'''










































