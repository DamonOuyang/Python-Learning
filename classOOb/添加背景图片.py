
'''
import tkinter
win=tkinter.Tk()
label1=tkinter.Label(win,text="AA1",bg="blue")
label2=tkinter.Label(win,text="AA2",bg="red")
label3=tkinter.Label(win,text="AA2",bg="yellow")
label4=tkinter.Label(win,text="AA2",bg="green")
#表格布局无法使用，不在使用pack() 赛满
#表格
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
label4.grid(row=1,column=1)

# label1.pack()
# label2.pack()
# label3.pack()
# label4.pack()
win.mainloop()
'''
'''
import tkinter
win=tkinter.Tk()
bt=tkinter.Listbox(win)
bt.pack(fill=tkinter.Y,side=tkinter.RIGHT) # side 贴边
bt.pack(fill=tkinter.Y,side=tkinter.LEFT) # side 贴边
win.mainloop()
'''
'''
import tkinter
win=tkinter.Tk()
label=tkinter.Label(win,text="AAA1",bg="blue")
labe2=tkinter.Label(win,text="AAA2",bg="red")
labe3=tkinter.Label(win,text="AAA3",bg="yellow")
label.pack()
labe2.pack()
labe3.pack()
win.mainloop()
'''
'''
import tkinter
win=tkinter.Tk()
label1=tkinter.Label(win,text="AA1",bg="blue",fg="yellow")
label1.place(x=10,y=10,anchor=tkinter.NW)
win.mainloop()
'''
'''
import tkinter
win=tkinter.Tk()
label=tkinter.Label(win,text="hell天朝",
                    font=("华文彩云",256),
                    fg="yellow",
                    bg="blue")# 给字体添加 前景色 背景色 字体大小等
label.pack()
win.mainloop()
'''
# 添加一个背景图片
# import tkinter
# win = tkinter.Tk()
# photo=tkinter.PhotoImage(file=r"E:\Python Learning\classOOb\1.jpg")#加载一张图片
# label=tkinter.Label(win,image=photo)#将图片添加到一个label中
# label.pack() # pack 有塞满的意思
# win.mainloop() # win 窗口进如消息循环


















