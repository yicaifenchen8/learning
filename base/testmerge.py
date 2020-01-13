import numpy

# 替换系统函数
oldPrint = print
print = lambda *args: oldPrint('-', *args)


# list 合并
x=[1]+[2,3]
print(x)

# map合并
x = {'1':1}
y = {'2':2}
z = dict(x, **y)
print(z)

x = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(x)
y = x[1:, :1]
print(y)

x = [1, 2, 3]
print(x[0:1])

# 元组合并
x = 1, 2, 3
print(x)
x += 4,5,6
print(x)
print(x[3:])
