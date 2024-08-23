#这个包用来发送电子邮件
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from config import EmailConfig

# 发送邮件
def SendEmail(sendmail,receiverMail,biaoti,neirong):
    """
    发送验邮件

    参数:
    sendmail (str): 发件地址
    receiverMail (str): 接收地址
    biaoti (str): 邮件标题
    neirong (str): 邮件内容

    返回:
    bool
    """
    message = MIMEText(neirong, 'html', 'utf-8') #格式化文本
    message['From'] = formataddr((EmailConfig.MailNick, sendmail))
    message['To'] = formataddr((None, receiverMail))
    message['Subject'] = biaoti

    try:
        # 连接 SMTP 服务器
        smtp_server = smtplib.SMTP(EmailConfig.MailHost, EmailConfig.MailPort)
        smtp_server.starttls()
        # 登录邮箱
        smtp_server.login(EmailConfig.MailUser,EmailConfig.MailPass)
        # 发送邮件
        smtp_server.sendmail(sendmail, [receiverMail], message.as_string())
        # 退出 SMTP 连接
        smtp_server.quit()
        return True
    except Exception as e:
        print("邮件发送失败:", e)
        return False
