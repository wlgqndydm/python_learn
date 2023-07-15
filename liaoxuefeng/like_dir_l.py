#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request

# response = urllib.request.urlopen("https://www.baidu.com")
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))
# txt = response.read().decode("utf-8")

import os
from time import sleep

def make_dir_info(dir_path):
    dir_path = os.path.abspath(dir_path)
    out_s = ""
    out_s += str( os.stat(dir_path).st_mode) + "\t"
    out_s += str( os.stat(dir_path).st_uid) + "\t"
    out_s += str( os.stat(dir_path).st_gid) + "\t"
    out_s += str( os.stat(dir_path).st_size) + "\t"
    out_s += str( os.stat(dir_path).st_mtime) + "\t"
    out_s += str(os.path.split(dir_path)[1]) + "\t"

    print(out_s)

def dir_l():
    all_dir = [x for x in os.listdir() if os.path.isdir(x)]
    [make_dir_info(x) for x in all_dir]
    print(all_dir)

dir_l()