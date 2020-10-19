import pytest

t = 12345, 54321, 'hello!'

def test_simple():
    assert (0) == 0


def test_simple1():
    empty = ()
    assert len(empty) == 0


def test_simple2():
    p = (1, 2)
    assert len(p) == 2


def test_tuple1():
    assert t[0] == 12345


def test_tuple2():
    assert t == (12345, 54321, 'hello!')


def test_tuple3():
    u = t, (1, 2, 3, 4, 5)
    assert u == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))


@pytest.mark.parametrize(
    'test_case',
    [
        ('t[0]', (8888)),
    ]
)
def test_tuple4(test_case):
    a = set(test_case[0])
    assert a != test_case[1]


def test_tuple5():
    v = ([1, 2, 3], [3, 2, 1])
    assert v == ([1, 2, 3], [3, 2, 1])



