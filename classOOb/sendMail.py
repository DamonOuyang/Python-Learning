'''
import smtplib #发邮件
from email.mime.text import MIMEText#邮件文本

class SendMail:
    def __init__(self,SMTPSever,Sender,password):
        self.SMTServer = "smtp.163.com" # 服务器
        self.Sender = "OuYangDaMeng@163.com" #发送邮件的地址
        self.passWord = "dimonoy" #密码

        self.mailSever = smtplib.SMTP(self.SMTServer,25) # 邮件服务器25端口
        self.mailSever.login(self.Sender,self.passWord) # 登陆
    def SendMsg(self,Message,title,mailList):
        msg =MIMEText(Message) # 转化邮件文本
        msg["Subject"]=title #邮件标题
        msg["From"]=self.Sender #邮件发送者
        msg["To"]="825824032@qq.com"#谁来收
        self.mailSever.sendmail(self.Sender,
                                mailList,
                                msg.as_string())

    def exit(self):
        self.mailSever.quit()

sender1=SendMail("smtp.163.com","OuYangDaMeng@163.com","dimonoy")
sender1.SendMsg("你好你借我的钱什么时候还","在不还我没钱吃饭了",["825824032@qq.com"])
sender1.exit()
'''
# 测试成功
import smtplib  #发邮件
from  email.mime.text import MIMEText #邮件文本
class  SendMail:
    def __init__(self,SMTPsever,Sender,password ):
        # self.SMTPsever = "smtp.163.com"  # 服务器
        # self.Sender = "yincheng8848@163.com"  # 发送邮件的地址
        # self.password = "tsinghua8848"  # 密码
        # self.Sender = "OuYangDaMeng@163.com"
        # self.password = "dimonoy888"  # 密码
        # self.mailsever = smtplib.SMTP(self.SMTPsever, 25)  # 邮件服务器25端口
        # self.mailsever.login(self.Sender, self.password)  # 登陆
        self.mailsever = smtplib.SMTP(SMTPsever, 25)  # 邮件服务器25端口
        self.mailsever.login(Sender, password)  # 登陆

    def Send(self,Sender,Message,title,maillist):
        msg = MIMEText(Message)  # 转化邮件文本
        msg["Subject"] =title  # 邮件标题
        msg["From"] = Sender  # 邮件发送者
        msg["To"] = "yincheng8848@163.com"  # 谁来收
        # msg["To"] = "OuYangDaMeng@163.com"   # 谁来收
        self.mailsever.sendmail(Sender,
                           maillist,
                           msg.as_string())

    def exit(self):
        self.mailsever.quit()

# sender1= SendMail("smtp.163.com","yincheng8848@163.com","tsinghua8848")
sender1= SendMail("smtp.163.com","OuYangDaMeng@163.com","dimonoy888")
sender1.Send("OuYangDaMeng@163.com","发送邮件测试","邮件内容",["OuYangDaMeng@163.com","825824032@qq.com"])
sender1.exit()




















