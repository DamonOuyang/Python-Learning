'''
#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎访问W3Cschool教程！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

'''
'''
import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('192.168.10.90',9999))
s.listen(5)
while 1:
    try:
        clientsock,clientaddr=s.accept()
    except Exception as err:
        print(err)
    while 1:
        data=clientsock.recv(1024)
        time.sleep(1)
        if not data:
            break
        clientsock.send(("hello,it's my computer").encode())
        print('client address:'+str(clientaddr))
        clientsock.close()
'''