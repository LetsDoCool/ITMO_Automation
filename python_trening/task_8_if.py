# программа проверяет является число положительным
# или отрицательным и выводит соответствующее сообщение

# num = 3

# Также попробуйте следующие варианты значения num
# num = -5
num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


# str_2 содержит в себе str_1 ?

str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('ДА')
else:
    print('НЕТ')


# str_2 содержит в себе str_1 ?

str_1 = 'test'
str_2 = 'test1'

def task(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')


