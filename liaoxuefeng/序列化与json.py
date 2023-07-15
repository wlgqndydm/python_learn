#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

with open("dump.txt","w",encoding="utf-8") as f:
    d = dict(name = "张三",age = 20,score = 88)
    json.dump(d,f,ensure_ascii=False)   #在此处的ensure_ascii=False 保证序列化的文字保持原文本，而不是转化为ascii码后存入。
    """ GitHub Copilot: 当`ensure_ascii`参数设置为`True`时，`json.dumps()`函数将确保所有非ASCII字符（即中文字符）都被转义为Unicode转义序列，例如`\uXXXX`。
    这意味着输出的JSON字符串中，所有中文字符都将被转义为Unicode编码，例如`\u5c0f\u660e`。这是默认设置。
    如果将`ensure_ascii`参数设置为`False`，则`json.dumps()`函数将不会对中文字符进行转义，而是直接输出中文字符。 """

with open("dump.txt","r",encoding="utf-8") as f:
    js2d = json.load(f)
    print(js2d,type(js2d))
    
    out = json.dumps(js2d,ensure_ascii=True)
    print(out)
    d = json.load(js2d)

with open("dump.txt","w",encoding="utf-8") as f:
    json.dump(d,f,ensure_ascii=False)
