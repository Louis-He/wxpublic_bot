# -*- coding: utf-8 -*-
import werobot
import time

robot = werobot.WeRoBot(token='louishe999617')

@robot.handler
def hello(message):
    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(message.time))
    print(message.source+' --> '+message.content)
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()