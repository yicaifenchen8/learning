# 装饰器-装饰class和方法---类似万能代理
def singleton(cls):
    instances = {}

    def inner():
        if cls not in instances:
            instances[cls] = cls()
        return cls

    return inner


def wrapper(func):
    def checker(x, y, *args, **kwargs):
        if x < 0 or y < 0:
            return 0
        else:
            return func(x, y)

    return checker

# 可变参数
# *args要么是表示调用方法大的时候额外的参数可以从一个可迭代列表中取得
# **kwargs来表明，所有未被捕获的关键字参数都应该存储在kwargs的字典中
def logger(func):
    def inner(*args, **kwargs):
        # print("Arguments were: ", args, kwargs)
        print("Arguments were: %s,%s" %(args, kwargs))
        return func(*args, **kwargs)

    return inner


@singleton
class TestSingletonClass(object):
    pass


@singleton
def testSingletonMethod():
    pass


print(testSingletonMethod(), testSingletonMethod() == testSingletonMethod())
print(TestSingletonClass(), TestSingletonClass() == TestSingletonClass())


@logger
@wrapper
def add(x=0, y=0):
    return x + y


print(add(-1, + 5, a=0))
