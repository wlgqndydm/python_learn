#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

global_dict = {}
local_school = threading.local()

class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.fenshu = 80

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print(f"Hello, {std} (in {threading.current_thread().name})")

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=("Alice",),name="Thread-A")
t2 = threading.Thread(target=process_thread,args=("Bob",),name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()

