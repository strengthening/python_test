#-*- coding:utf-8 -*-

class Singleton(type):

    def __init__(cls,name,base,dict):
        super(Singleton , cls).__init__(name, base ,dict)
        cls._instance = None

    def __call__(cls,*args,**kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance



class MyClass(object):
    __metaclass__ = Singleton


if __name__ == '__main__':

    one = MyClass()
    two = MyClass()

    assert one == two