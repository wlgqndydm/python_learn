#!/usr/bin/env python3
# -*- coding:utf-8 -*-
d = dict(name="bob",age=20,score=88)
d["name"]  = "张三"
import pickle
# print(pickle.dumps(d))
f = open("dump.txt","wb")
pickle.dump(d,f)
f.close()

f = open("dump.txt","w",encoding="utf-8")
import json
# print(json.dumps(d,ensure_ascii=False))
json.dump(d,f,ensure_ascii=False)
with open("dump.txt","r",encoding="utf-8") as f:
    print(f.read())

class Student(object):
    def __init__(self,name,age,score) -> None:
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        "name":std.name,
        "age":std.age,
        "score":std.score
    }

s = Student("张三",20,88)
json_str = json.dumps(s,default=lambda obj:obj.__dict__, ensure_ascii=False)
print(json_str)
def dict2student(d):
    return Student(d["name"],d["age"],d["score"])

print(zs := json.loads(json_str,object_hook=dict2student))
print(zs.name)