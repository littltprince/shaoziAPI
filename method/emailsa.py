##encoding:utf-8
import os
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
Uesr=opconfig().OpConfig(filePath,'EMAILS','user')
Password=opconfig().OpConfig(filePath,'EMAILS','password')
Sender=opconfig().OpConfig(filePath,'EMAILS','sender')
Receiver=opconfig().OpConfig(filePath,'EMAILS','receiver')
Smtpserver=opconfig().OpConfig(filePath,'EMAILS','smtpserver')
def send_email(html_msg):
    """发送邮件的脚本"""
    # 邮件服务信息，个人
    # smtp_server = 'smtp.163.com'
    # username = "lihua.0221@163.com"
    # password = 'xxxxx'  # 授权码，并不是邮箱登陆密码

    # 邮件服务信息，公司
    smtp_server =Smtpserver
    username = Uesr
    password = Password  # 授权码，企业163的就是登陆密码

    # 邮件发送和接收人
    sender =Sender
    receiver =Receiver

    # 邮件头信息
    msg = MIMEMultipart('related')
    msg['Subject'] = Header("勺子课堂api测试报告")
    msg["From"] = sender
    msg['To'] = ','.join(receiver)  # 这里要注意

    html_msg = \
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1>这是一封python写的邮件，使用的是HTML格式构造正文</h1>
        <h2>可以为文字添加超链接，比如：<a href="https://www.jianshu.com/u/8159970c6959">简书-小溏</a></h2>
        <hr>
        <h3>还可以添加图片，比如下面这张</h3>
        <img src="https://pub-static.haozhaopian.net/assets/projects/export/jpg/29736970-a991-4b91-91af-854a8eb561e6.jpg">
        </body>
        </html>
        """

    # html 内容
    content_html = MIMEText(html_msg, "html", "utf-8")
    msg.attach(content_html)

    # report_file_path = reportpath
    # # 构造附件，测试成功，附件有很多类型，现在构建的是xlsx文件
    # attach_table = MIMEApplication(open(report_file_path, 'rb').read())
    # # 给附件增加标题
    # attach_table.add_header('Content-Disposition', 'attachment',filename='我的附件.html')
    # #  这样的话，附件名称就可以是中文的了，不会出现乱码
    # attach_table.set_charset('utf-8')
    # msg.attach(attach_table)

    # 发送邮件，测试成功，流程都是固定的：创建客户端，登陆，发送，关闭
    email_client = smtplib.SMTP(smtp_server)
    email_client.login(username, password)
    email_client.sendmail(sender, receiver, msg.as_string())
    email_client.quit()

if __name__ == '__main__':
    send_email(reportpath)