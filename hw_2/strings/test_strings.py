import pytest

a = 'qwerty'


def test_str1():
    assert a[-2] == 't'


def test_str2():
    assert len(a) == 6


def test_str3():
    assert a.count('r') == 1


def test_str4():
    assert a.upper() == 'QWERTY'

@pytest.mark.parametrize(
    'test_case',
    [
        ('abracadabra', 'aca'),
    ]
)
def test_str5(test_case):
    a = test_case[0]
    assert a[3:6] == test_case[1]