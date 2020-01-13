import yaml

# 动态修改方法 1
class A:
    def f(self):
        print(1)

def ff(self):
    print(2)
A.f = ff

a = A()
a.f()

# 动态修改方法 2
# class A:
#     def f(self):
#         print(1)
#
# oldF = A.f
# def newF(self):
#     oldF(self)
#     print(2)
# A.f = newF
#
# a = A()
# a.f()




# yaml
# f = open('res/config/server.yaml', encoding='utf-8')
# config = yaml.load(f)
# f.close()
#
# print(config['ip'])
# print(config['port'])
# print(config)


# 动态修改方法
class A:
    def f(self):
        print(self)

class B(A):
    def f(self):
        A.f(self)#调用父类方法

b = B()
b.f()