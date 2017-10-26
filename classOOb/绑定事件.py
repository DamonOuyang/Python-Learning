
'''
# 鼠标位置
import tkinter

def call(event):
    print(event.x,event.y)

win=tkinter.Tk()
frame=tkinter.Frame(win,width=200,height=200)
frame.bind("<Motion>",call) # 激发的函数，监控当前窗口的位置(鼠标进入移动的位置)


frame.pack()
win.mainloop()
'''

'''
#键盘按键事件
import tkinter

def call(event):
    print(event.keysym)

win=tkinter.Tk()
frame=tkinter.Frame(win,width=200,height=200) # 限定范围，不显示
frame.bind("<Key>",call) # 按下按键 按键激发函数
frame.focus_set() # 获取焦点

frame.pack()
win.mainloop()
'''


# import tkinter
# def  call(event):
#     print(event.keysym)# 或取 键盘系统
# win=tkinter.Tk()
# frame=tkinter.Frame(win,width=200,height=200) #限定范围，不显示
# frame.bind("<Key>",call) #激发的函数
# frame.focus_set()  #获取焦点
# frame.pack()
# win.mainloop()




'''
# 鼠标响应事件
import tkinter

def call(event):
    print(event.x,event.y)

win=tkinter.Tk()

frame=tkinter.Frame(win,width=200,height=200)
frame.bind("<Button-1>",call) # 绑定激发的函数
frame.bind("<Button-2>",call) # 绑定激发的函数
frame.bind("<Button-3>",call) # 绑定激发的函数
frame.pack()

win.mainloop()
'''





























































