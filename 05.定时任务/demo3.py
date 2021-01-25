#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :demo3.py
@说明        :
@时间        :2021/01/25 13:36:01
@作者        :张强
@版本        :1.0
'''


"""
    3.使用sched模块，python内置模块，它是一个调度(延时处理机制),每次想要定时执行任务都必须写入一个调度
    使用步骤：(1)生成调度器 s = sched.scheduluer(time.time,time.sleep) 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞
    (2)加入调度时间，

"""

# 初始化sched模块的 scheduler类
# 第一个参数是可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞
import sched
import time
from datetime import datetime
schedule = sched.scheduler(time.time, time.sleep)
# 被周期性调度触发的函数


def printTime(inc):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    schedule.enter(inc, 0, printTime, (inc,))

# 默认60秒


def main():
    # enter四个参数分别为：间隔事件、优先级(用于同时间到底的两个事件同时执行时定序)、被调用触发的函数
    # 给该触发函数的参数(tuple形式)
    schedule.enter(0, 0, printTime, (inc,))
    schedule.run()


# 10s 输出一次
main(10)
