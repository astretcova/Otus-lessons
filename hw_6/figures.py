from math import pi


class Figure:
    name = None
    angles = None

    def tell(self):
        print(f'Name: {self.name}. Angels: {self.angles}')

    def add_area(self, other):
        assert isinstance(y, Figure), 'Argument other is not Figure'
        return round(self.area() + other.area(), 2)

    def area(self):
        raise NotImplemented

    def perimeter(self):
        raise NotImplemented


class Circle(Figure):
    name = 'Circle'
    angles = 0

    def __init__(self, r):
        self.r = abs(r)

    def area(self):
        return round(pi * self.r ** 2, 2)

    def perimeter(self):
        x = 2 * pi * self.r
        return round(x, 2)


class Rectangle(Figure):
    name = 'Rectangle'
    angles = 4

    def __init__(self, a, b):
        self.a = abs(a)
        self.b = abs(b)

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    name = 'Square'

    def __init__(self, a):
        super().__init__(a, a)


class Triangle(Figure):
    name = 'Triangle'
    angles = 3

    def __init__(self, a, b, c):
        self.a = abs(a)
        self.b = abs(b)
        self.c = abs(c)

    def area(self):
        p = self.perimeter() / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return round(s)

    def perimeter(self):
        x = self.a + self.b + self.c
        return x
