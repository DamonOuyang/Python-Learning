import tkinter
from  tkinter  import ttk

def go(*args): #处理事件
    print(comboxlist.get()) #选中当前的值

win=tkinter.Tk() #构造窗体
win.geometry("800x800+300+0")

comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist=ttk.Combobox(win,textvariable=comvalue) #初始化
comboxlist["values"]=("1","2","3","4")
comboxlist.current(0)#选择第一个
comboxlist.bind("<<ComboboxSelected>>",go) #绑定事件

comboxlist.pack()
win.mainloop() #进入消息循环

'''
import tkinter
import os

def shutdown():
    os.system("shutdown -s -t 20000")

def cancelShutdown():
    os.system("shutdown -a")

win=tkinter.Tk() #构造窗体
win.title("Hello world")
win.geometry("800x800+300+0")

button=tkinter.Button(win,text="shutdown",command=shutdown)#收到消息执行这个函数
button.pack()#加载到窗体

button1=tkinter.Button(win,text="cancel",command=cancelShutdown)#收到消息执行这个函数
button1.pack()#加载到窗体

button2=tkinter.Button(win,text="Hello",command=lambda :print("hello world"),width=50,height="30")#收到消息执行这个函数
button2.pack()#加载到窗体

win.mainloop()#进入消息循环
'''















































