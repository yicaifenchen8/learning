def test(a: bool, b: str) -> bool: print(a, b)


def test2(a: bool, b: str) -> bool:
    print(a, b)


t = lambda a, b: print(a, b)
a = lambda: 1 if 0 else 0
b = lambda a, b: a + b

test(1, 3)
t(1, 2)
print(a())
print(b(1, 2))
