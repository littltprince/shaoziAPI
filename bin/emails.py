#encoding:utf-8
import smtplib
import os
from email.mime.text import MIMEText  # MIMEText()定义邮件正文
from email.header import Header  # Header()定义邮件标题


# 发送邮箱服务器
smtpserver = 'smtp.exmail.qq.com'

# 发送邮箱用户/密码(登录邮箱操作)
user = "mengdebin@shaoziketang.com"
password = "6FA2vbbCGEhenDVD"

# 发送邮箱
sender = "mengdebin@shaoziketang.com"

# 接收邮箱
receiver = "1124479307@qq.com"

# # 发送主题
# subject = 'love'

# # 编写HTML类型的邮件正文（把HTML代码写进入）
# msg = MIMEText('<html><body><a href="">测试报告</a></p></body></html>', report, 'utf-8')
# msg['Subject'] = Header(subject, 'utf-8')
#
# # 连接发送邮件（smtplib模块基本使用格式）
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(user, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    mail_msg = """
    <p>勺子课堂测试报告...</p>
    <p><a href=".\result_report.html">测试报告地址</a></p>
    """
    msg = MIMEText(mail_msg, 'html', 'utf-8')
    msg['From'] = Header("测试负责人", 'utf-8')
    msg['To'] = Header("各位大佬", 'utf-8')

    subject = '勺子课堂测试报告'
    msg['Subject'] = Header(subject, 'utf-8')
    # msg = MIMEText(mail_body, 'html', 'utf-8')
    # msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')  # 邮箱服务器
    smtp.login(user, password)  # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")
