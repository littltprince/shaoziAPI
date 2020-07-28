#encoding:utf-8
import os
import time
base_dir=os.path.dirname(os.path.dirname(__file__))
filePath=os.path.join(base_dir,'configs/test_case.config')
from method.ReadConfig import opconfig
reportpath=os.path.join(base_dir,'bin/result_report.html')
re="./bin/result_report.html"
print(reportpath)
# 导入相关库-email
from email.mime.multipart import MIMEMultipart  # 构建邮件头信息，包括发件人，接收人，标题等
from email.mime.text import MIMEText  # 构建邮件正文，可以是text，也可以是HTML
from email.mime.application import MIMEApplication  # 构建邮件附件，理论上，只要是文件即可，一般是图片，Excel表格，word文件等
from email.header import Header  # 专门构建邮件标题的，这样做，可以支持标题中文

import smtplib
Uesr=opconfig().OpConfig(filePath,'EMAILS','user')
Password=opconfig().OpConfig(filePath,'EMAILS','password')
now=time.strftime('%y-%m-%d_%H-%M-%S')
Sender=opconfig().OpConfig(filePath,'EMAILS','sender')
Receiver=opconfig().OpConfig(filePath,'EMAILS','receiver')
Smtpserver=opconfig().OpConfig(filePath,'EMAILS','smtpserver')

class sende_mail:
    def sendemails(self,email_to,filepath):
        #---邮件的信息配置
        msg=MIMEMultipart()
        msg['Subject']=now+'测试报告'
        msg['From']=Sender
        msg['To']=';'.join(Receiver)
        #---文字部分
        part=MIMEText('本次的测试结果如下')
        msg.attach(part)
        #---增加附件
        part=MIMEApplication(open(filepath,'rb').read())
        part.add_header('Content-Disposition','attachment',filename=filepath)
        msg.attach(part)
        try:
            s=smtplib.SMTP(Smtpserver,timeout=465)
            # s.connect(Smtpserver,timeout=465)
            s.login(Uesr,Password)
            s.sendmail(Sender,email_to,msg.as_string())
            s.quit()
            print("邮件已发出")
        except smtplib.SMTPException as e:
            print("error",e)

if __name__ == '__main__':
    sende_mail().sendemails(Receiver,r'C:\Users\勺子课堂\PycharmProjects\shaoziketang\bin\result_report.html')
