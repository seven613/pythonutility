"""
    2.使用县城定时器Timer  
    原理：指定时间间隔后启动线程，执行线程函数；
    场景：完成定时任务，如：定时提醒，定时发送，定时采集功能等

timer = threading.Timer(interval,function,args=None,kwargs=None)
    参数：interval - 定时器间隔，间隔多少秒之后启动定时器任务(单位：秒);
        function - 线程函数;
        args - 线程参数，可以传递元组类型数据，默认为空
        kwargs -线程参数,可以传递字典类型数据，默认为空
    主要方法：
        Timer(interval,function,args=None,kwargs=None) 创建定时器
        cancel()  取消定时器
        start() 使用线程方式执行
        join(self,timeout=None) 等待线程执行结束
"""
import threading


def thred_Timer():
    print("该起床了，5秒之后再次呼叫你起床")
    # 声明全局变量
    global t1
    t1 = threading.Timer(5, thred_Timer)
    t1.start()


# 声明全局变量
if __name__ == '__main__':
    # 创建并初始化线程
    t1 = threading.Timer(5, thred_Timer)
    # 启动线程
    t1.start()
