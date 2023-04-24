# Задача 1
num = [14, 20]
max_number = max(num)


def task_1(num):
    return max_number


print('Наибольшее число', max_number)


# Задача 2
a = 125
b = -10
c = 135


def task_2(a, b, c):
    return a, b, c


if a - b == c or b - a == c:
    print('YES')
else:
    print('NO')


# Задача 3
month = 8


def season(month):
    return month


if 1 <= month <= 2 or month == 12:
    print('winter')
elif 3 <= month <= 5:
    print('spring')
elif 6 <= month <= 8:
    print('summer')
elif 9 <= month <= 11:
    print('autumn')


# Задача 4
a = 11
b = 9
c = 1


def arb(a, b, c):
    return a, b, c


if a > 10 and b > 10 and c > 10:
    print('YES')
else:
    print('NO')


# Задача 5
x = [-10, 4, -16, 167, 17]
count = 0


def pos(x):
    return x


for i in x:
    if i > 0:
        count += 1

print(count)


# Задача 6
years = int(3)
months = int(1)
days = 29
y = years * months * days
m = months * days


def d(y, m):

    return y + m


print(d(y, m))
