import tkinter
import os
def go():
    print(entry.get())
    if entry.get() == "记事本":
        os.system("notepad")

win=tkinter.Tk()
win.geometry("400x400+0+0")
entry=tkinter.Entry(win)# input
entry.pack()
entry.place(x=0,y=0)
button=tkinter.Button(win,text="搜索",command=go) # command 为按键点击响应的毁掉函数
#button.pack()
button.place(x=200,y=0)
win.mainloop()















































