#!/usr/bin/env python3
# -*- coding:utf-8 -*=

class Student(object):
    def __init__(self, name = "Michael") -> None:
        self.name = name

    def __str__(self):
        return "Student object (name:%s)" % self.name

    __repr__ = __str__
    def __getattr__(self,attr):
        if attr == "score":
            return 99
        if attr == "age":
            return lambda:25
        raise AttributeError("'Student' object has no attribute '%s'" % attr)

    def __call__(self):
        print("My name is %s." % self.name)


if __name__ == "__main__":
    print(Student("Michael"))


class Fib(object):
    def __init__(self) -> None:
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

class Chain(object):
    def __init__(self,path = "") -> None:
        self._path = path

    def __getattr__(self,path):
        return Chain("%s/%s" % (self._path,path))

    def __str__(self) -> str:
        return self._path

    __repr__ = __str__

# for n in Fib():
#     print(n)
a = Fib()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[10])
print(a[100])
print(a[1:10])
s = Student()
print(s.name)
print(s.score)
print(s.age())
# print(s.aaa)
print(Chain().status.user.timeline.list )
s()
# print(callable(Student()))
