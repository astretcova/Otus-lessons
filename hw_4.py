import pytest
import jsonschema
import requests


id_MAX = 200

todo_response = {
    'type': 'object',
    'properties': {
        'userId': {'type': 'integer'},
        'id': {'type': 'integer'},
        'title': {'type': 'string'},
        'completed': {'type': 'boolean'},
    },
    'required': ['userId', 'id', 'title', 'completed'],
    'additionalProperties': False,
}

get_todos_response_schema = {
    'type': 'array',
    'items': todo_response,
}


@pytest.fixture
def todos_url():
    return 'https://jsonplaceholder.typicode.com/todos'


@pytest.fixture(scope="module")
def session():
    return requests.Session()


def test_get_todos(session, todos_url):
    response = session.get(todos_url)
    assert response.status_code == 200, response.text
    todos = response.json()
    assert len(todos) == id_MAX
    print(todos)

    jsonschema.validate(todos, get_todos_response_schema)


@pytest.mark.parametrize('id',
                         [1, id_MAX, 100])
def test_get_positive(session, todos_url, id):
    res = session.get(url=f'{todos_url}/{id}')

    assert res.status_code == 200, res.text
    assert res.json()['id'] == id


@pytest.mark.parametrize('id',
                         [0, -1, 201])
def test_get_negative(session, todos_url, id):
    res = session.get(url=f'{todos_url}/{id}')

    assert res.status_code == 404, res.text
    assert not res.json()


@pytest.mark.parametrize(
    'user_id, expected_len',
     [
         (1, 20),
         (2, 20),
         (10, 20),
         (0, 0),
         (11, 0)
     ]
)  # todo: проверить фильтрацию по другим параметрам
def test_get_filtering(session, todos_url, user_id, expected_len):
    res = session.get(url=f'{todos_url}?userId={user_id}')

    assert res.status_code == 200, res.text
    todos = res.json()
    assert len(todos) == expected_len, res.text
    for todo in todos:
        assert todo['userId'] == user_id

    jsonschema.validate(todos, get_todos_response_schema)


def test_post_negative(session, todos_url):
    payload = {"title": '1', "completed": True, "userId": 1}
    res = session.post(url=f'{todos_url}/1', json=payload)

    assert res.status_code == 404


@pytest.mark.parametrize(
    'id, title, complited, user_id',
    [
        (201, '', True, 1),
        (202, '123', False, 2),
        (300, 'abc', False, 10),
    ]
)
def test_post_positive(session, todos_url, id, title, complited, user_id):
    payload = {'id': id, 'title': title, 'complited': complited, 'userId': user_id}
    res = session.post(url=todos_url, json=payload)

    assert res.status_code == 201, res.text
    j = res.json()
    assert j['id'] == id_MAX + 1
    assert j['userId'] == user_id
    assert j['title'] == title
    assert j['complited'] == complited


def test_put(session, todos_url):
    title = 'qwerty'
    completed = 'true'
    payload = {'title': title, 'completed': completed, 'id': 1}
    res = session.put(url=f'{todos_url}/{id}', json=payload)

    assert res.status_code == 500, res.text


@pytest.mark.parametrize(
    'userId, id, title, completed, expected_status',
    [
        (1, 1, 'qwert', False, 200),
        (1, 200, 'qwert', False, 200),
        (1, 0, 'qwert', False, 500),
        (1, -1, 'qwert', False, 500),
        (1, 201, 'qwert', False, 500),
    ]
)
def test_put_todos(session, todos_url, userId, id, title, completed, expected_status):
    payload = {'title': title, 'completed': completed, 'userId': userId, 'id': id}
    res = session.put(url=f'{todos_url}/{id}', json=payload)

    assert res.status_code == expected_status
    if str(expected_status)[0] == '2':
        j = res.json()
        assert j['id'] == id
        assert j['userId'] == userId
        assert j['title'] == title
        assert j['completed'] == completed
        jsonschema.validate(j, todo_response)


@pytest.mark.parametrize(
    'id, field, value',
    [
        (1, 'title', 'test title'),
        (100, 'complete', False),
        (200, 'userId', 2),
    ]
)
def test_patch_todos(session, todos_url, id, field, value):
    payload = {field: value}
    res = session.put(url=f'{todos_url}/{id}', json=payload)
    assert res.status_code == 200
    j = res.json()
    assert j[field] == value


def test_delete(session, todos_url):
    res = session.delete(url=f'{todos_url}/1')

    assert res.status_code == 200
    assert not res.json()
