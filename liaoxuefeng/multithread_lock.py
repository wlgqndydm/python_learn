#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time,threading
import multiprocessing,os
lock:threading.Lock = threading.Lock()

# 银行存款
balance = 0

def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        # 先要获取锁
        lock.acquire()
        try:
            #放心的改
            change_it(n)
        finally:
            #改完后释放锁
            lock.release()

if __name__ == "__main__" :
    t1 = threading.Thread(target=run_thread,args=(5,))
    t2 = threading.Thread(target=run_thread,args=(8,))
    t3 = threading.Thread(target=run_thread,args=(10,))
    t4 = threading.Thread(target=run_thread,args=(12,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(balance)