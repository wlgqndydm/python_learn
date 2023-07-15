#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#学自廖雪峰的python教程：https://www.liaoxuefeng.com/wiki/1016959663602400/1017631559645600#0
#并按照其中的部分提示做了修改。
import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
def r_task_queue():
    # global task_queue
    return task_queue

#接收结果的队列
result_queue = queue.Queue()
def r_result_queue():
    # global result_queue
    return result_queue

# 从BaseManager继承的QueueManager，必须在最外面
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上,callable参数关联了Queue对象：
QueueManager.register("get_task_queue",callable=r_task_queue)
QueueManager.register("get_result_queue",callable=r_result_queue)

if __name__ == "__main__":

    #绑定端口5000，设置验证码“abc”
    manager = QueueManager(address=("127.0.0.1",5000),authkey=b"abc")
    #启动Queue
    manager.start()

    #获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    #放几个任务进去
    for i in range(10):
        n = random.randint(0,10000)
        print("Put task %d..." % n)
        task.put(n)

    #从result队列读取结果
    print("Try get results...")
    for i in range(10):
        r = result.get(timeout=30)
        print("Result:%s" % r)

    #关闭
    manager.shutdown()
    print("master exit")