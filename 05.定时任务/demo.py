#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :demo.py
@说明        :定时任务
@时间        :2021/01/25 11:03:43
@作者        :张强
@版本        :1.0
'''

# 1.使用线程睡眠函数Sleep()方法,简单粗暴，一直占用CPU,阻塞线程，不建议使用

from datetime import datetime
import time

'''每隔10秒打印当前时间'''


def timedTask():
    while True:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(10)


if __name__ == '__main__':
    timedTask()
