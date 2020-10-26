import pytest


class Rectangle:
    name = 'Rectangle'
    angles = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


@pytest.mark.parametrize(
    'a, b, perimeter',
    [
        (3, 4, 14)
    ]
)
def test_Rectangle_perimeter(a, b, perimeter):
    instance = Rectangle(a, b)
    assert instance.perimeter() == perimeter


@pytest.mark.parametrize(
    'a, b, area',
    [
        (3.0, 4.5, 13.5)
    ]
)
def test_Rectangle_area(a, b, area):
    instance = Rectangle(a, b)
    assert instance.area() == area


@pytest.mark.parametrize(
    'a, b',
    [
        (3.0, 4)
    ]
)
def test_Rectangle(a, b):
    instance = Rectangle(a, b)
    assert instance.a == a
    assert instance.b == b


def test_name():
    assert Rectangle.name == "Rectangle"


def test_angles():
    assert Rectangle.angles == 4

