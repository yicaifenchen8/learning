from functools import reduce


print('\n-----------------stream--------------')
l = [i * i for i in range(10) if i % 2 == 0]
print(l)

l.sort(key=lambda e: e, reverse=True)
print(l)

ret = filter(lambda e: e > 10, l)
print(list(ret))

ret = map(lambda e: e - 2, l)
print(list(ret))

ret = reduce(lambda a, b: a + b, [1, 3, 4], 0)
print(ret)
