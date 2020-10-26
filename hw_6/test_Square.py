import pytest


class Square:
    name = 'Square'
    angles = 4

    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return 4 * self.a



@pytest.mark.parametrize(
    'a, perimeter',
    [
        (3.0, 12)
    ]
)
def test_Square_perimeter(a, perimeter):
    instance = Square(a)
    assert instance.perimeter() == perimeter


@pytest.mark.parametrize(
    'a, area',
    [
        (3, 9)
    ]
)
def test_Square_area(a, area):
    instance = Square(a)
    assert instance.area() == area


@pytest.mark.parametrize(
    'a',
    [
        (3)
    ]
)
def test_Square(a):
    instance = Square(a)
    assert instance.a == a


def test_name():
    assert Square.name == "Square"


def test_angles():
    assert Square.angles == 4