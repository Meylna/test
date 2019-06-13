import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender = 'kongxaiolin@163.com'
receiver = 'kongdemei23@163.com'
smtpserver = 'smtp.163.com'
password = 'kongdemei23'


def send_Mail(file_new,result):
    f = open(file_new, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    try:
        smtp = smtplib.SMTP(smtpserver, 25)
        smtp.login(sender, password)
        msg = MIMEMultipart()
        # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
        # 发送正文
        text = MIMEText(mail_body, 'html', 'utf-8')
        # 定义邮件正文标题
        text['Subject'] = Header('API自动化测试报告', 'utf-8')
        msg.attach(text)
        # 发送附件
        # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
        msg['Subject'] = Header('[执行结果：' + result + ']'+ 'API自动化测试报告', 'utf-8')
        msg_file = MIMEText(mail_body, 'html', 'utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_file)
        msg['From'] = 'kongxaiolin<kongxaiolin@163.com>'
        msg['To'] = "kongdemei23<kongdemei23@163.com>"
        tmp = smtp.sendmail(sender, receiver, msg.as_string())
        print(tmp)
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print(str(e))
        return False

#print(s