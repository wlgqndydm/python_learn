#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def name_of_email(addr:str):
    m = re.compile(r"^(\<[\S ]+?\>\s+?\S+?|\S+?)@\S+")
    result = m.match(addr).groups()
    if '<' in result[0]:
        result = re.match(r"\<([\S ]+?)\>",result[0]).group(1)
    else:
        result = result[0]
    return result

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')