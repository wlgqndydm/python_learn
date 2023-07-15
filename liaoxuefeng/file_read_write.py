#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import time
try:
    f = open("ceshi.txt","r",encoding="utf8",errors="ignore")
    
except FileNotFoundError as e:
    print(e)
else:
    # c = f.read(1)
    # while c != "":
    #     print(c,end="")
    #     time.sleep(1)
    #     c = f.read(1)
    txt = f.read()
    f.close()
    with open("ceshi.txt","a",encoding="UTF8") as f:
        f.write(txt * 2)