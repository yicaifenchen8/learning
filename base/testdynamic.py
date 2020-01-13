from functools import reduce

print('\n-----------------dynamic--------------')
str = '''
def p(*args):
    print(args)
'''

exec(str)
p(1, 2, 3)

print(eval('1+2'))

add = compile('2+3', '', 'eval')
print(eval(add))

defp = compile(str, '', 'exec')
print(exec(defp))
p(1)


class User:
    pass


cls = User
user = cls()
print('user', user)

user = eval('User')()
print('user', user)


