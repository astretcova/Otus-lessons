import pytest

from .figures import Circle


@pytest.mark.parametrize(
    'r, perimeter',
    [
        (3, 18.85),
        (-10, 62.83)

    ]
)
def test_circle_perimeter(r, perimeter):
    instance = Circle(r)
    assert instance.perimeter() == perimeter


@pytest.mark.parametrize(
    'r, area',
    [
        (3, 28.27),
        (-10, 314.16)
    ]
)
def test_circle_area(r, area):
    instance = Circle(r)
    assert instance.area() == area


@pytest.mark.parametrize(
    'r',
    [3.0, -10, 0]
)
def test_circle(r):
    instance = Circle(r)
    assert instance.r == abs(r)


def test_name():
    x = Circle(1)
    assert x.name == "Circle"


def test_angles():
    x = Circle(1)
    assert x.angles == 0