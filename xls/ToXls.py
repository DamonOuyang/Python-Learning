import datetime
import time
import os
import sys
import xlwt #需要的模块

#<file target-language="Chinese">
#</file>


f = open("C:\\Users\\AndroidDev\\Desktop\\lang_std.xml","r")
lines = f.readlines()#读取全部内容
for line in lines:
    print(line)

class  filegetlines:
    def __init__(self,filepath):
        self.filepath=filepath
        self.file=open(filepath,"rb")
        self.Lines=-1

    def readlines(self):
        i=0
        while True:
            linestr=self.file.readline()
            if  linestr:#不为空，
                linestr=linestr.decode("utf-8")
                print(linestr, end="")

                i+=1
            else:
                #为空
                break
        self.Lines=i
        return i

# f1= filegetlines("C:\\Users\\AndroidDev\\Desktop\\lang_std.xml")
# print(f1.readlines())


















