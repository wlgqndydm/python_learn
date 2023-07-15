#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Animal(object):
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print("Running...")

class FlyableMixIn(object):
    def fly(self):
        print("Flying...")

class CarnivorousMixIn(object):
    def carnivorous(self):
        print("Carnivorousing...")

class HerbivoresMixIn(object):
    def herbivores(self):
        print("Herbivoresing...")



#各种动物
class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass

class Bat(Mammal,FlyableMixIn):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


#tcp和多线程的MixIn模式
from socketserver import *
from threading import *


class MyTCPServer(TCPServer,ThreadingTCPServer):
    pass
