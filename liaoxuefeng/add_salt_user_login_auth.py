#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib,random

""" 加盐的用户登录认证 """

def calc_md5(password:str):
    md = hashlib.md5()
    md.update(password.encode("utf-8"))
    md5 = md.hexdigest()
    return md5
    # return hashlib.md5(password.encode("utf-8")).hexdigest()  #高手的写法

class User(object):
    def __init__(self,username,password) -> None:
        self.username = username
        self.salt = "".join([chr(random.randint(48,122)) for i in range(20)])
        self.password = calc_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def get_md5(user:User,pws):
    md5o = hashlib.md5()
    s = pws + user.salt
    md5o.update(s.encode("utf-8"))
    md5 = md5o.hexdigest()
    return md5

def login(username,password):
    user = db[username]
    return user.password == get_md5(user,password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')