import pytest
from math import pi


class Circle:
    name = 'Circle'
    angles = 0

    def __init__(self, r):
        self.r = r

    def area(self):
        return round(pi * self.r ** 2, 2)

    def dlina_okr(self):
        x = 2 * pi * self.r
        return round(x, 2)


@pytest.mark.parametrize(
    'r, dlina_okr',
    [
        (3, 18.85)
    ]
)
def test_Circle_dlina_okr(r, dlina_okr):
    instance = Circle(r)
    assert instance.dlina_okr() == dlina_okr


@pytest.mark.parametrize(
    'r, area',
    [
        (3, 28.27)
    ]
)
def test_Circle_area(r, area):
    instance = Circle(r)
    assert instance.area() == area


@pytest.mark.parametrize(
    'r',
    [
        (3.0)
    ]
)
def test_Circle(r):
    instance = Circle(r)
    assert instance.r == r


def test_name():
    assert Circle.name == "Circle"


def test_angles():
    assert Circle.angles == 0