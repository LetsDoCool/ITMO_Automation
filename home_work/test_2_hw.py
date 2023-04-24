# Задача 1
a: int = 1
b: float = 123.124
c: str = 'string'
d: list = [1, 2, 3]
e: bool = 10 < 5


def task_1(a, b, c, d, e):
    return a, b, c, d, e


print(a, ' = ', type(a), ',', b, ' = ', type(b), ',', c, ' = ', type(c),  ',', d , ' = ', type(d), ',', e, ' = ', type(e))


# Задача 2
def task_2(a: list):
    a = [1, 2, 3, 5, 8, 13, 21]
    return a


print(a)

