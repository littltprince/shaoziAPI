#encoding:utf-8
import os
import time
base_dir=os.path.dirname(os.path.dirname(__file__))
filePath=os.path.join(base_dir,'configs/test_case.config')
from method.ReadConfig import opconfig
reportpath=os.path.join(base_dir,'bin/result_report.html')

# 导入相关库-email
from email.mime.multipart import MIMEMultipart  # 构建邮件头信息，包括发件人，接收人，标题等
from email.mime.text import MIMEText  # 构建邮件正文，可以是text，也可以是HTML
from email.mime.application import MIMEApplication  # 构建邮件附件，理论上，只要是文件即可，一般是图片，Excel表格，word文件等
from email.header import Header  # 专门构建邮件标题的，这样做，可以支持标题中文
import smtplib
now=time.strftime('%Y-%m-%d %H:%M:%S')
# User=opconfig().OpConfig(filePath,'EMAILS','user')
# Password=opconfig().OpConfig(filePath,'EMAILS','password')
# Sender=opconfig().OpConfig(filePath,'EMAILS','sender')
# Receiver=eval(opconfig().OpConfig(filePath,'EMAILS','receiver'))
# Smtpserver=opconfig().OpConfig(filePath,'EMAILS','smtpserver')

# 发送邮箱服务器
smtpserver="smtp.exmail.qq.com"
# 发送邮箱用户/密码(登录邮箱操作)
user="mengdebin@shaoziketang.com"
password = "s6siqg9jNHVCfa4"
# 发送邮箱
sender="mengdebin@shaoziketang.com"
# 接收邮箱
receiver=["@qq.com","@shaoziketang.com"]
class send_email:
    def sendemails(self,email_to,filepath):
        #---邮件的信息配置
        msg=MIMEMultipart()
        msg['Subject']=now+'测试报告'
        msg['From']=sender
        msg['To']=','.join(receiver)
        #---文字部分
        # part=MIMEText('本次的测试结果如下')
        # msg.attach(part)
        #---html部分
        html_msg = \
            """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            <h1>这是本次接口自动化的测试结果，请各位大佬查收，详情可点击链接或者附件</h1>
            <h2>结果:<a href="${url}">点击查看测试结果</a></h2>
            <hr>
            <h3>加油干鸭！！</h3>
            <img src="http://wx4.sinaimg.cn/large/007qPM5Ngy1g3cpqh9c53j30g40hkt9n.jpg">
            </body>
            </html>
            """
        if html_msg.find('${url}') != -1:
            html_msg = html_msg.replace('${url}', reportpath)
        # html 内容
        content_html = MIMEText(html_msg, "html", "utf-8")
        msg.attach(content_html)
        #---增加附件
        part=MIMEApplication(open(filepath,'rb').read())
        part.add_header('content-disposition', 'attachment', filename='shaozi测试报告.html',)
        msg.attach(part)
        try:
            s=smtplib.SMTP(smtpserver,timeout=465)
            # s.connect(Smtpserver,timeout=465)
            s.login(user,password)
            s.sendmail(sender,email_to,msg.as_string())
            s.quit()
            print("邮件已发出")
        except smtplib.SMTPException as e:
            print("error",e)



