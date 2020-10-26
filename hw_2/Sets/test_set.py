import pytest

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}


def test_simple():
    assert basket == {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}


def test_basket():
    assert 'apple' in basket


def test_basket1():
    assert 'crabgrass' not in basket

@pytest.mark.parametrize(
    'test_case',
    [
        ('abracadabra', {'a', 'r', 'b', 'c', 'd'}),
    ]
)
def test_set1(test_case):
    a = set(test_case[0])
    assert a == test_case[1]


@pytest.mark.parametrize(
    'test_case',
    [
        ('abracadabra', 'alacazam', {'r', 'd', 'b'}),
    ]
)
def test_set2(test_case):
    a = set(test_case[0])
    b = set(test_case[1])
    assert (a - b) == test_case[2]


@pytest.mark.parametrize(
    'test_case',
    [
        ('abracadabra', 'alacazam', {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}),
    ]
)
def test_set_letters_in_a_or_b_or_both(test_case):
    a = set(test_case[0])
    b = set(test_case[1])
    assert (a | b) == test_case[2]


def test_set4():
    a = set('abracadabra')
    b = set('alacazam')
    assert a & b == {'a', 'c'}


def test_set5():
    a = set('abracadabra')
    b = set('alacazam')
    assert a ^ b == {'r', 'd', 'b', 'm', 'z', 'l'}