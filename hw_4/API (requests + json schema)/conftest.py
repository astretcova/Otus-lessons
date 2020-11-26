import pytest
import requests


@pytest.fixture
def todos_url():
    return 'https://jsonplaceholder.typicode.com/todos'


@pytest.fixture(scope="module")
def session():
    return requests.Session()