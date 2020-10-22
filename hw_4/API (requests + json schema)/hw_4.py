import pytest
from jsonschema import validate
import json
import os

id_MAX = 200


def assert_valid_schema(data: dict, schema_file: str):
    with open(os.path.join(os.path.dirname(__file__),schema_file)) as f:
        schema = json.load(f)

    return validate(instance=data, schema=schema)


def test_get_todos(session, todos_url):
    response = session.get(todos_url)
    assert response.status_code == 200, response.text
    todos = response.json()
    assert len(todos) == id_MAX

    assert_valid_schema(todos, 'todo_list_schema.json')


def test_get_todo(session, todos_url):
    res = session.get(url=f'{todos_url}/1')
    todo = res.json()

    assert_valid_schema(todo, 'todo_schema.json')


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
         (10, 20)
     ]
)
def test_get_filtering_positive(session, todos_url, user_id, expected_len):
    res = session.get(url=f'{todos_url}?userId={user_id}')

    assert res.status_code == 200, res.text
    todos = res.json()
    assert len(todos) == expected_len, res.text
    for todo in todos:
        assert todo['userId'] == user_id

    #assert_valid_schema(todos, 'todo_list_schema.json')


@pytest.mark.parametrize(
    'user_id, expected_len',
     [
         (0, 0),
         (11, 0)
     ]
)
def test_get_filtering_negative(session, todos_url, user_id, expected_len):
    res = session.get(url=f'{todos_url}?userId={user_id}')

    assert res.status_code == 200, res.text
    todos = res.json()
    assert len(todos) == expected_len, res.text


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
    userid = 1
    title = 'qwerty'
    completed = 'true'
    payload = {'title': title, 'completed': completed, 'id': 1}
    res = session.put(url=f'{todos_url}/{userid}', json=payload)

    assert res.status_code == 200, res.text
    res_json = res.json()
    assert res_json['title'] == title
    assert res_json['completed'] == completed


@pytest.mark.parametrize(
    'userId, id, title, completed, expected_status',
    [
        (1, 1, 'qwert', False, 200),
        (1, 200, 'qwert', False, 200),
    ]
)
def test_put_positive(session, todos_url, userId, id, title, completed, expected_status):
    payload = {'title': title, 'completed': completed, 'userId': userId, 'id': id}
    res = session.put(url=f'{todos_url}/{id}', json=payload)

    assert res.status_code == expected_status

    j = res.json()
    assert j['id'] == id
    assert j['userId'] == userId
    assert j['title'] == title
    assert j['completed'] == completed

        #assert_valid_schema(j, 'todo_schema.json')


@pytest.mark.parametrize(
    'userId, id, title, completed, expected_status',
    [
        (1, 0, 'qwert', False, 500),
        (1, -1, 'qwert', False, 500),
        (1, 201, 'qwert', False, 500),
    ]
)
def test_put_negative(session, todos_url, userId, id, title, completed, expected_status):
    payload = {'title': title, 'completed': completed, 'userId': userId, 'id': id}
    res = session.put(url=f'{todos_url}/{id}', json=payload)

    assert res.status_code == expected_status


@pytest.mark.parametrize(
    'id, field, value',
    [
        (1, 'title', 'test title'),
        (100, 'completed', True),
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
