# определяем функцию
def add(x, y):
    return x + y


# вызываем функцию
add(1, 2)


# вызываем функцию
print(add(1, 2))

def add(x, y):
    return x + y


# вызываем функцию
print(add(1, 2))


# вызываем функцию с другими аргументами
print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))


print(arg(2, 2))


# print(arg(2, 2, '1', 1))


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))


print(range_arg('1', '2', d='3', c='4'))


def arg(a = (1, 2, 3, 4)):
    return a[0]

print(arg())


def arg2(radius, Pi=3.14159):
    return Pi * radius * radius

print(arg2(2))