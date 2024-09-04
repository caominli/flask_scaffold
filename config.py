#配置文件
class Config(object):
    DEBUG = True #调试模式
    SECRET_KEY = '' #密钥


#数据库配置
class DataConfig(object):
    name = 'test' #数据库名
    user = '' #用户名
    password = '' #密码
    host = 'localhost' #主机
    port = 5432 #端口

#管理员配置
class AdminConfig(object):
    username = '' #用户名
    password = '' #密码

#邮件服务器配置
class EmailConfig(object):
    MailHost = '' #邮件服务器
    MailPort = 587 #端口
    MailUser = '' #用户名
    MailPass = '' #密码
    MailNick = '' #WEB名称
    SendEmail = '' #发送通知的邮箱地址
   
