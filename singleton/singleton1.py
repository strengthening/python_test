#-*- encoding=utf-8 -*-  

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls,'_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1


if __name__ == '__main__':

    a = MyClass()
    b = MyClass()

    a.a = 3

    print 'a.a = ' , a.a
    print 'b.a = ' , b.a

    print 'b.a == a.a  is ' , b.a == a.a
    print 'b.a is a.a  is ' , b.a is a.a