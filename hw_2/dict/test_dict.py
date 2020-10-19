import pytest


@pytest.fixture
def tel():
    return {'jack': 4098, 'sape': 4139}


@pytest.mark.parametrize(
    'key',
    ['jack', 'sape']
)
def test_dict_del(tel, key):
    del tel[key]
    assert key not in tel
    assert tel != {}


def test_simple_dict():
    assert {} == dict()


@pytest.mark.parametrize(
    'value',
    [4127, 'abra', None, Exception]
)
def test_dict_set_guido(tel, value):
    tel['guido'] = value
    assert tel['guido'] == value


def test_dict2(tel):
    assert tel['jack'] == 4098


def test_dict3(tel):
    del tel['sape']
    tel['irv'] = 4127
    assert tel == {'irv': 4127, 'jack': 4098}


@pytest.mark.parametrize(
    'key, value, del_key',
    [
        ['jack', 100500, None],
        ('sape', 'mhgjhg', None),
        ('lekjvk',  13, 'jack'),
    ]
)
def test_set2(tel, key, value,  del_key):
    tel[key] = value
    assert tel[key] == value

    if del_key is not None:
        del tel[del_key]
    assert del_key not in tel



