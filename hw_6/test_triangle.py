import pytest


class Triangle:
    name = 'Triangle'
    angles = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return round(s)

    def perimeter(self):
        x = self.a + self.b + self.c
        return x


@pytest.mark.parametrize(
    'a, b, c, perimeter',
    [
        (3, 4, 2, 9)
    ]
)
def test_Triangle_perimeter(a, b, c, perimeter):
    q = Triangle(a, b, c)
    assert q.perimeter() == perimeter


@pytest.mark.parametrize(
    'a, b, c, area',
    [
        (3, 4, 2, 3)
    ]
)
def test_Triangle_area(a, b, c, area):
    instance = Triangle(a, b, c)
    assert instance.area() == area


@pytest.mark.parametrize(
    'a, b, c',
    [
        (3, 4, 2)
    ]
)
def test_Triangle(a, b, c):
    instance = Triangle(a, b, c)
    assert instance.a == a
    assert instance.b == b
    assert instance.c == c


def test_name():
    assert Triangle.name == "Triangle"


def test_angles():
    assert Triangle.angles == 3