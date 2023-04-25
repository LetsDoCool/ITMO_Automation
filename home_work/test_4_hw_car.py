#
class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return 'Автомобиль заведен'

    def turn(self):
        return 'Автомобиль заглушен'

    def car_year(self):
        return f'Год выпуска автомобиля: {self.year}'

    def car_type(self):
        return f'Тип автомобиля: {self.type}'

    def car_color(self):
        return f'Цвет автомобиля: {self.color}'


car = Car('blue', 'sedan', '2019')


print(Car.start(car))
print(Car.turn(car))
print(Car.car_year(car))
print(Car.car_type(car))
print(Car.car_color(car))
