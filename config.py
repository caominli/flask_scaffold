#配置文件
class Config(object):
    DEBUG = True #调试模式
    SECRET_KEY = 'BxBp_0LdE2xbqFQp1pLguHL8MvtwGSKEPj4P8g6faBM=' #密钥


#数据库配置
class DataConfig(object):
    name = 'test' #数据库名
    user = 'mymuzixin' #用户名
    password = 'Mzx16838638' #密码
    host = 'localhost' #主机
    port = 5432 #端口

#管理员配置
class AdminConfig(object):
    username = 'muxiaoliang' #用户名
    password = 'banban123' #密码

#邮件服务器配置
class EmailConfig(object):
    MailHost = 'smtp.qq.com' #邮件服务器
    MailPort = 587 #端口
    MailUser = 'ocid1.user.oc1..aaaaaaaayk54ezouawzhephsrlser3yoct3xfnaemiqw5naetibc4rezpmdq@ocid1.tenancy.oc1..aaaaaaaap3vd45hus3hlenc3llyajgzfydbcrlzx3rx4fqpbz3emdnplp2qq.dm.com' #用户名
    MailPass = 'jmxJ1jVBfd8UHKBU1:fd' #密码
    MailNick = '木小良' #WEB名称
    SendEmail = 'info@btcmai.com' #发送通知的邮箱地址
   