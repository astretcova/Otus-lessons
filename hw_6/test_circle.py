from math import pi
import pytest


class Circle:
    name = 'Circle'
    angles = 0

    def __init__(self, r):
        self.r = r

    def area(self):
        return round(pi * self.r ** 2, 2)

    def perimeter(self):
        x = 2 * pi * self.r
        return round(x, 2)


@pytest.mark.parametrize(
    'r, perimeter',
    [
        (3, 18.85)
    ]
)
def test_circle_perimeter(r, perimeter):
    instance = Circle(r)
    assert instance.perimeter() == perimeter


@pytest.mark.parametrize(
    'r, area',
    [
        (3, 28.27)
    ]
)
def test_circle_area(r, area):
    instance = Circle(r)
    assert instance.area() == area


@pytest.mark.parametrize(
    'r',
    [
        (3.0)
    ]
)
def test_circle(r):
    instance = Circle(r)
    assert instance.r == r


def test_name():
    x = Circle(1)
    assert x.name == "Circle"


def test_angles():
    x = Circle(1)
    assert x.angles == 0