# Задача
course = input('На каком курсе Вы обучаетесь (введите число)? ')
number = int(course)

if 5 > number > 0:
    print('Вы бакалавр')
elif 4 < number < 7:
    print('Вы магистр')
elif 6 < number < 10:
    print('Вы аспирант')
else:
    print('Введите корректный год обучения')


# Задача

a = 10

if a > 100 or a < 100:
    print('-')
else:
    print('+')