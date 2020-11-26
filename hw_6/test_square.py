import pytest

from .figures import Square


@pytest.mark.parametrize(
    'a, perimeter',
    [
        (3.0, 12),
        (-2, 8)
    ]
)
def test_square_perimeter(a, perimeter):
    instance = Square(a)
    assert instance.perimeter() == perimeter


@pytest.mark.parametrize(
    'a, area',
    [
        (3, 9),
        (-3, 9)
    ]
)
def test_square_area(a, area):
    instance = Square(a)
    assert instance.area() == area


@pytest.mark.parametrize(
    'a',
    [3, -4]
)
def test_square(a):
    instance = Square(a)
    assert instance.a == abs(a)


def test_name():
    instance = Square(1)
    assert instance.name == "Square"


def test_angles():
    instance = Square(1)
    assert instance.angles == 4