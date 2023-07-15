#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# import logging
# logging.basicConfig(level=logging.INFO)


""" def foo(s):
    n = int(s)
    assert n != 0,"n is zero!"
    # print(">>>n = %d" % n)
    return 10/n

def main():
    foo("0")
main() """
import pdb

s = "0"
n = int(s)
pdb.set_trace()
# logging.info("n = %d" %n)
print(10/n)