#huey是个单独的模块，并需要运行一个消费者程序，消费者程序运行时指向本文件的huey实列
#在其他文件中调用任务时，导入本文件的huey实列即可

from huey import crontab,SqliteHuey #导入定时任务
# # 创建一个SqliteHuey实例
huey = SqliteHuey(filename='task.db')
# huey = PriorityRedisHuey('huey') #创建一个RedisHuey实例

#导入时间模块
import time

#定义一个发送验证码任务，该任务需要被调用才会执行
@huey.task()
def sendcode():
    #被调用的程序
    # SendEmail(EmailConfig.SendEmail,sendmail,f'来自的{EmailConfig.MailNick}验证码','您的验证码是：'+code)
    print('执行了一次发送验证码')


#定义一个周期性任务，该任务会每天12点执行一次
@huey.periodic_task(crontab(hour=12))
def datetask():
    print('现在是12点')

#定义一个周期性任务，每12小时执行一次
@huey.periodic_task(crontab(hour='*/12'))
def datetask2():
    print('已经过去12小时')

#定时一个定期循环任务，每分钟执行一次
@huey.periodic_task(crontab(minute='*/1'))
def printtask():
    print('现在时间是2：',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))



"""
最好huey消费者程序比flask先启动

开发运行消费者程序:
huey_consumer.py app.task.huey -w 2

添加sendcode任务到队列，设置优先级为10:
huey.enqueue(sendcode.s(priority=10))
"""