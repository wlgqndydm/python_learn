#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum,unique

Month: Enum = Enum(
    "Month",
    (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
)

@unique
class Weekday(Enum):
    Sun = 0 #Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# for name,member in Month.__members__.items():
#     print(name,"=>",member,",",member.value)
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

g = Gender(1)
g.Male= 222 #实际上，这里新加了一个叫Male的属性
print(g.Male)
g.name = "aaaaa"    #枚举类的属性是不能修改的，这里会报错。
print(g.name)