import json

a = {'a': 1}
print(a)
d = [{'d': a}]
ds = json.dumps(d)
print('dumps-', ds)
print('loads-', json.loads(ds))

d = [a, a, {'aa': a}]
print('d', d)
