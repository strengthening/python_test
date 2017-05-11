#-*- encoding=utf-8 -*-

'''
    装饰器 单例
'''

def singleton(cls):
    instance = cls()
    instance.__call__ = lambda : instance
    return instance


@singleton
class MyClass():
    x = 100


'''
    上面的代码定义了一个 singleton 装饰器，覆盖了类的 __call__ 方法， 
    该方法会在类创建的时候创建一个类的实例，并在之后类每次的实例化时总是返回这个实例对象。
'''
if __name__ == '__main__':

    mc1 = MyClass()
    mc2 = MyClass()
    
    assert mc1 == mc2