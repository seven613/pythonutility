#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :demo4.py
@说明        :APScheduler 调度
@时间        :2021/01/25 13:38:53
@作者        :张强
@版本        :1.0
'''
'''
    ApScheduler 全称Advanced Python Scheduler，轻量级的python定时任务调度框架。
    支持三种调度任务：固定时间间隔，固定时间点，Linux下的Crontab命令。还支持一部执行、后台执行调度任务

    使用步骤：
        (1)新建一个调度器 schedulers
        (2)添加一个调度任务 job stores
        (3)运行调度任务
    ApScheduler 有四个嘴贱，分别是：调度器scheduler,作业存储job store,触发器trigger,执行器executor
    调度器scheduler:它是任务调度器，属于控制器角色，它配置作业存储器和执行器可以在调度器中完成，例如添加、修改和移除作业
    触发器triggers:描述调度任务被触发的条件，不过触发器完全是无状态的
    作业存储器job stores:任务持久化仓库，默认保存任务在内存中，也可将任务保存在各种数据库中，任务中的数据序列化后存到持久化数据库，
                        从数据库加载后反序列化
    执行器executors:负责处理作业的运行，他们通常通过在作业中提交指定的可调用对象到一个线程或进程池来进行。当作业完成时，执行器将会通知调度器
    
'''




import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
def timedTask():
    print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])


if __name__ == '__main__':
    # 创建后踢执行的schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为timedTask,触发器选择interval间隔性,间隔时长为2秒
    scheduler.add_job(timedTask, 'interval', seconds=2)
    # 启动调度任务
    scheduler.start()
    while True:
        print(time.time())
        time.sleep(5)
