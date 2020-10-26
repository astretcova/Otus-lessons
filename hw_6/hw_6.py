from math import pi


class Figure:
    name = None
    angles = None

    def tell(self):
        print(f'Name: {self.name}. Angels: {self.angles}')

    def add_area(self, y):
        self.name = x
        self.name = y
        return round(x.area() + y.area(), 2)

    def __instancecheck__(self, instance):
        pass


class Triangle(Figure):
    name = 'Triangle'
    angles = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s

    def perimeter(self):
        x = self.a + self.b + self.c
        return x


class Rectangle(Figure):
    name = 'Rectangle'
    angles = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Figure):
    name = 'Square'
    angles = 4

    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return 4 * self.a


class Circle(Figure):
    name = 'Circle'
    angles = 0

    def __init__(self, r):
        self.r = r

    def area(self):
        return round(pi * self.r ** 2, 2)

    def dlina_okruznosti(self):
        return round(2 * pi * self.r, 2)


x = Circle(3)
y = Square(2)
y.tell()
print(x.area())
print(y.area())
#print(x.dlina_okruznosti())  #18.85

print(x.add_area(y))

