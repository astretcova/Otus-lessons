import pytest

from .figures import Triangle


@pytest.mark.parametrize(
    'a, b, c, perimeter',
    [
        (3, 4, 2, 9),
        (-4, -2, 6, 12)
    ]
)
def test_triangle_perimeter(a, b, c, perimeter):
    q = Triangle(a, b, c)
    assert q.perimeter() == perimeter


@pytest.mark.parametrize(
    'a, b, c, area',
    [
        (3, 4, 2, 3),
        (-4, 2, 6, 0)
    ]
)
def test_triangle_area(a, b, c, area):
    instance = Triangle(a, b, c)
    assert instance.area() == area


@pytest.mark.parametrize(
    'a, b, c',
    [
        (3, 4, 2),
        (-4, -2, 6)
    ]
)
def test_triangle(a, b, c):
    instance = Triangle(a, b, c)
    assert instance.a == abs(a)
    assert instance.b == abs(b)
    assert instance.c == abs(c)


def test_name():
    instance = Triangle(1, 2, 1)
    assert instance.name == "Triangle"


def test_angles():
    instance = Triangle(1, 2, 1)
    assert instance.angles == 3