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


print('\n--------class---------------')
user = User()
user.name = 'ycf'
user.age = 30
User.testStatic();
print(user)
print(user.d)
print(user.aaaa)
user(1, 2)

# __doc__   表示类的描述信息
# __module__表示当前操作的对象在那个模块
# __class__ 表示当前操作的对象的类是什么
# __init__  构造方法，通过类创建对象时，自动触发执行
# __call__  对象后面加括号，触发执行。
# __dict__  类或对象中的所有成员
# __name__  类，方法，属性名
# __str__   如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值。
# __setitem__，__getitem__，__delitem__  用于索引操作，如字典。分别表示获取、设置、删除数据
print('\n--------__xxx__---------------')
print(user.__dict__)
print(user.__class__)
print(user.__dir__())
print(user.__str__())
print(user.test.__name__)
print(User.__name__)

print('\n--------reflect---------------')
print(getattr(user, 'name'))
setattr(user, 'name', 'good')
print(getattr(user, 'name'))
f = getattr(user, 'test')
f()