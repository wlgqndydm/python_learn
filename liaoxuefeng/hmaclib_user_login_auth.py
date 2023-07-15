#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 使用hmac库制作的用户登录认证 """

import hmac, random

def hmac_md5(key:str, s:str):
    return hmac.new(
        key=key.encode("utf-8"), msg=s.encode("utf-8"), digestmod="md5"
    ).hexdigest()

class User(object):
    def __init__(self,username,password) -> None:
        self.username = username
        self.key = "".join([chr(random.randint(48,122)) for i in range(20)])
        self.password = hmac_md5(self.key,password)
        
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user = db[username]
    return user.password == hmac_md5(user.key,password)

    # 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')