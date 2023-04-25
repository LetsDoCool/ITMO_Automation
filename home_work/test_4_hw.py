# Задача 1
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        a1 = int(self.width) * int(self.height)
        return a1

    def perimeter(self):
        p1 = (int(self.width) + int(self.height)) * 2
        return p1


a = Rectangle('10', '12')
b = Rectangle('124', '78')
c = Rectangle('56', '1')

print(Rectangle.area(a), 'см2')
print(Rectangle.perimeter(a), 'см')
print(Rectangle.area(b), 'см2')
print(Rectangle.perimeter(b), 'см')
print(Rectangle.area(c), 'см2')
print(Rectangle.perimeter(c), 'см')


# Задача 2
class Math:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)


    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


num = Math('7', '8')

print(Math.addition(num))
print(Math.multiplication(num))
print(Math.division(num))
print(Math.subtraction(num))


# Задача 3
class Clickbar:

    def __init__(self, text, type='Кнопка', locator=None):
        self.text = text
        self.type = type
        self.locator = locator

    def button(self):
        print(self.text, self.type)

    def click(self):
        return f'Клик по кнопке {self.text}'


text = Clickbar('Text')
check = Clickbar('Check Box')
radio = Clickbar('Radio Button')
web = Clickbar('Web Tables')
buttons = Clickbar('Buttons')
links = Clickbar('Links')
broken = Clickbar('Broken Links - Images')
upload = Clickbar('Upload and Download')
dynamic = Clickbar('Dynamic Properties')


text.button()
print(Clickbar.click(text))
check.button()
print(Clickbar.click(check))
radio.button()
print(Clickbar.click(radio))
web.button()
print(Clickbar.click(web))
text.button()
print(Clickbar.click(text))
buttons.button()
print(Clickbar.click(buttons))
links.button()
print(Clickbar.click(links))
broken.button()
print(Clickbar.click(broken))
upload.button()
print(Clickbar.click(upload))
dynamic.button()
print(Clickbar.click(dynamic))
