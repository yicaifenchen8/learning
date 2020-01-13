import math

f = math.sqrt
print(f(4))

f = lambda: print('lambda')
f()

def t():
    def f():
        return 1

    return f

print(t())
