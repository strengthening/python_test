#-*- coding:utf8 -*-

class A(object):

    def foo(self , x):
        print "executing foo(%s,%s)" % (self,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x

    @classmethod
    def class_foo(cls , x):
        print "executing class_foo(%s,%s)" % (cls,x)


if __name__ == '__main__':

    a = A()


    '''
    下面是一个对象实体调用方法的常用方式.对象实体a被隐式的传递给了第一个参数.
    '''
    a.foo(1)
    # executing foo(<__main__.A object at 0x7f237d15f7d0>,1)


    '''
    这种调用方法即上种方式的显式调用方法
    '''
    A.foo(a,1)
    # executing foo(<__main__.A object at 0x7f237d15f7d0>,1)


    '''
    用classmethods装饰,隐藏的传递给第一个参数的是对象实体的类(class A)而不是self.
    '''
    a.class_foo(1)
    # executing class_foo(<class '__main__.A'>,1)


    '''
    你也可以用类调用class_foo.实际上,如果你把一些方法定义成classmethod,那么实际上你是希望用类来调用这个方法,而不是用这个类的实例来调用这个方法.A.foo(1)将会返回一个TypeError错误,A.class_foo(1)将会正常运行:
    '''
    A.class_foo(1)
    # executing class_foo(<class '__main__.A'>,1)


    '''
    用staticmethods来装饰,不管传递给第一个参数的是self(对象实体)还是cls(类).它们的表现都一样:
    '''
    a.static_foo(1)
    # executing static_foo(1)
    A.static_foo('hi')
    # executing static_foo(hi)

    '''
    总结，self是实例对象，在定义类成员函数self必须是第一个参数，使用实例对象调用时，实例对象本身会被隐式传入方法；
         cls是类本身，在调用classmethod时候，类本身会被隐式传给方法的第一个参数
    '''