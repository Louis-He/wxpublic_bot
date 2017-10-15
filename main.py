# -*- coding: utf-8 -*-
import werobot
import time
#from apscheduler.schedulers.background import BackgroundScheduler

robot = werobot.WeRoBot(token='louishe999617')

@robot.handler
def hello(message):
    ts = '['+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(message.time))+']'
    print(ts + message.source+' --> '+message.content)
    return 'Hello World!'

'''
def clearlog():
    #clear logs every hour
    f = open('/home/weather/hsefz_server/wxbot/record/txtrecord.txt', 'w')
    f.write('[' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']record重新写入')
    f.close()  # you can omit in most cases as the destructor will call it
    print('[' + time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + ']record重制完成')

scheduler = BackgroundScheduler()
scheduler.add_job(clearlog, 'interval', seconds = 3600 * 6)#间隔6小时执行一次
scheduler.start()    #这里的调度任务是独立的一个线程
'''
# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()