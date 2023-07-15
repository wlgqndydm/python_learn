#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import multiprocessing as mp

def run_proc(name):
    print("Run chile process %s (%s)..." % (name,os.getpid()))

if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = mp.Process(target=run_proc,args=("test",))
    print("Child process will start.")
    p.start()
    p.join()
    print("Child process end.")