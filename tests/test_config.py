import pytest

from src.config import config


@pytest.fixture
def database():
    with open('test_database.ini', 'wt') as file:
        file.write('[postgresql]\n')
        file.write('host=localhost\n')
        file.write('database=database_name\n')
        file.write('user=user_name\n')
        file.write('password=user_password\n')


def test_config(database):
    with open('test_database.ini', 'rt') as file:
        data = config('test_database.ini')
        assert data['host'] == 'localhost'
        assert data['database'] == 'database_name'
        assert data['user'] == 'user_name'
        assert data['password'] == 'user_password'

    with pytest.raises(Exception):
        data = config('sample.ini')
