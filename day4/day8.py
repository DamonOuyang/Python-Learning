'''
print("hello world")
print('hello python')
print("""程序猿的读书历程：
x 语言入门 —>
 x 语言应用实践 —>
  x 语言高阶编程 —>
   x 语言的科学与艺术 —>
    编程之美 —>
     编程之道 —>
      编程之禅—>
      颈椎病康复指南""")
'''
'''
#bytes
#10
#_  _  _  _   _   _   _  _  byte 2^8=256     2^7=128,其中一个用于表示正负

b=bytes(1) #byte转化为二进制编码，1个字节
print(b) #\x16进制   2^4=16  8位  1个字节B
#1GB =1024MB =1024*1024KB =1024*1024*1024B*8位
'''
'''
#utf-8
a=bytes("你abc","utf-8") #不同的编码大小不一样内容不一样
print(a)
a=bytes("你好中国abc","gbk")
print(a)
'''
'''
#utf-8两个字符表示汉字，一个字符汉字结束，3个字符
print(bytes("我","utf-8"))
print(bytes("我的","utf-8"))
print(bytes("我的喔","utf-8"))

#GBK两个字符表示汉字，没有结束
print(bytes("我","gbk"))
print(bytes("我的","gbk"))
print(bytes("我的喔","gbk"))
'''
'''
mystr="hello python"
mystrc="hello 中国"
print(mystr.encode("utf-8"))
print(mystrc.encode("utf-8"))#encode返回二进制，用于写入文本
print(b'hello python'.decode("utf-8"))   #将二进制转化为文本
print(b'hello \xe4\xb8\xad\xe5\x9b\xbd'.decode("utf-8"))
print(b'hello python'.decode("gbk"))

#英文的东西，任何编码无所谓， GBK，UTF-8对于英文编码
#汉字注意编码的格式，不同的编码结果不一样，同样的二进制，换一种编码一般解析出错
'''
'''
print(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\xad\xe5\x9b\xbd'.decode("utf-8","ignore"))
#"ignore"，解码失败，强行解码
'''
'''
mystr="孙播	陈慧	申凌瑞	 陈慧  李佳奇	吴东	牛兴杰	"
print(mystr.index("陈慧")) #index查找字符串是否存在，存在返回第一个下标，不存在，异常错误
print(mystr.rindex("陈慧")) #rindex查找，返回最后一个的下表
#print(mystr.index("陈慧",7,10)) #第二个开始，第三个结束

'''

from string import Template #string文件导入Template
print(type(Template))
mystr=Template("hi,$name  你是  $baby")
print(mystr.substitute(name="何丰成",baby="lovely babay"))


















