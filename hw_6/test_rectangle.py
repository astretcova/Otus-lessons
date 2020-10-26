import pytest

from .figures import Rectangle


@pytest.mark.parametrize(
    'a, b, perimeter',
    [
        (3, 4, 14),
        (0.1, -4, 8.2)
    ]
)
def test_rectangle_perimeter(a, b, perimeter):
    instance = Rectangle(a, b)
    assert instance.perimeter() == perimeter


@pytest.mark.parametrize(
    'a, b, area',
    [
        (3.0, 4.5, 13.5),
        (1, -3, 3)
    ]
)
def test_rectangle_area(a, b, area):
    instance = Rectangle(a, b)
    assert instance.area() == area


@pytest.mark.parametrize(
    'a, b',
    [
        (3.0, 4),
        (0, 4)
    ]
)
def test_rectangle(a, b):
    instance = Rectangle(a, b)
    assert instance.a == a
    assert instance.b == b


def test_name():
    instance = Rectangle(1, 1)
    assert instance.name == "Rectangle"


def test_angles():
    instance = Rectangle(1, 1)
    assert instance.angles == 4

