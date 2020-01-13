class Proxy(object):

    def __init__(self, target):
        self.target = target

    def __getattribute__(self, name):
        target = object.__getattribute__(self, "target")
        attr = object.__getattribute__(target, name)

        def newAttr(*args, **kwargs):  # 包装
            print("before ", name)
            res = attr(*args, **kwargs)
            print("after ", name)
            return res

        return newAttr


class Descriptor(object):
    def __get__(self, obj, type=None):
        return 'get', self, obj, type

    def __set__(self, obj, val):
        print('set', self, obj, val)

    def __delete__(self, obj):
        print('delete', self, obj)


class User(object):
    fields = {}
    d = Descriptor()
    name = ''
    age = 0

    # set
    def __setattr__(self, key, value):
        print('set', key, value)
        self.fields[key] = value
        super.__setattr__(self, key, value)

    # get-找不到的属性会调用--实现万能对象不定义属性--调用时全走这个方法
    def __getattr__(self, item):
        if (not self.fields.__contains__(item)):
            self.fields[item] = {}
        print('get', item)
        return self.fields[item]

    # invoke
    def __call__(self, *args):
        print('call', args)

    # toString
    def __str__(self):
        return self.__dict__.__str__()

    def test(self):
        print('test')

    @staticmethod
    def testStatic():
        print('test')


print('\n--------proxy---------------')
proxy = Proxy(User())
proxy.test()
