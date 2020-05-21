from abc import *


class Test:
    @abstractmethod
    def m1(self):
        print('Hello')


t = Test()
t.m1()

# Hello
