# import tkinter
# from  tkinter import ttk  #导入内部包
# win=tkinter.Tk()
# tree=ttk.Treeview(win)#表格
#
#
# tree["columns"]=("姓名","年龄","身高")
# tree.column("姓名",width=100)   #表示列,不显示
# tree.column("年龄",width=100)
# tree.column("身高",width=100)
#
# tree.heading("姓名",text="姓名-name")#显示表头
# tree.heading("年龄",text="年龄-age")
# tree.heading("身高",text="身高-tall")
#
# tree.insert("",0,text="line1" ,values=("1","2","3")) #插入的行数
# tree.insert("",1,text="line1" ,values=("1","2","3"))
# tree.insert("",2,text="line1" ,values=("1","2","3"))
# tree.insert("",3,text="line1" ,values=("1","2","3"))
#
# tree.pack()
# win.mainloop()


import tkinter
from tkinter import ttk #导入内部包
win=tkinter.Tk()
tree=ttk.Treeview(win)#表格

tree["columns"]=("姓名","年龄","身高")
tree.column("姓名",width=100)#表示列,不显示
tree.column("年龄",width=100)
tree.column("身高",width=100)

# tree["columns"]=("姓名","年龄","身高")
# tree.column("姓名",width=100)   #表示列,不显示
# tree.column("年龄",width=100)
# tree.column("身高",width=100)

tree.heading("姓名",text="姓名-name")#显示表头
tree.heading("年龄",text="年龄-age")#显示表头
tree.heading("身高",text="身高-height")#显示表头

tree.insert("",0,text="line1",values=("1","2","3"))#插入的行数
tree.insert("",1,text="line1",values=("1","2","3"))
tree.insert("",2,text="line1",values=("1","2","3"))
tree.insert("",3,text="line1",values=("1","2","3"))

tree.pack()
win.mainloop()





'''
import tkinter
win=tkinter.Tk()
text=tkinter.Text(win) # 文本编辑器
text.insert(tkinter.INSERT,"因为你在我心中是那么的具体")
text.insert(tkinter.INSERT,"\r\n")

text.insert(tkinter.INSERT,"因为你在我心中是那么的具体")
text.insert(tkinter.INSERT,"\r\n")

text.insert(tkinter.INSERT,"因为你在我心中是那么的具体")
text.insert(tkinter.INSERT,"\r\n")

text.insert(tkinter.INSERT,"因为你在我心中是那么的具体")
text.insert(tkinter.INSERT,"\r\n")

text.insert(tkinter.INSERT,"因为你在我心中是那么的具体")
text.insert(tkinter.INSERT,"\r\n")

text.pack()
win.mainloop()
'''

































