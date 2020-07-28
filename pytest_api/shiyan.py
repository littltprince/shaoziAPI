from email.mime.application import MIMEApplication
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
a=os.path.dirname(os.path.dirname(__file__))
report=os.path.join(a,'bin/result_report.html')
# 发送邮箱服务器
smtpserver="smtp.exmail.qq.com"
# 发送邮箱用户/密码(登录邮箱操作)
user="mengdebin@shaoziketang.com"
password = "s6siqg9jNHVCfa4Z"
# 发送邮箱
sender="mengdebin@shaoziketang.com"
# 接收邮箱
receiver="1124479307@qq.com"

em=MIMEMultipart()
em['Subject']='aaa'
em['Sender']=sender
em['To']=receiver

conent=MIMEText('hahhaha')
em.attach(conent)
app=MIMEApplication(open(report,'rb').read())
app.add_header('content-disposition', 'attachment', filename='mouo.html')
em.attach(app)
s=smtplib.SMTP()
s.connect(smtpserver)
s.login(user,password)
s.send_message(em)
s.quit()